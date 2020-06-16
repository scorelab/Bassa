import threading
import queue
from queue import Queue
import json, time
from DownloadManager import *
from Models import Status, Download
from EMail import send_mail
from DiskMan import *
from ConfReader import get_conf_reader
import logging
from MinioHandler import *

import websocket
import sys

conf = get_conf_reader("dl.conf")
db_lock = threading.Lock()
folder_size=0
startedDownloads = []
handlerLst = []
handler = None
mHandler = None
verbose = False
sc = None
messageQueue = Queue()

if len(sys.argv) == 2 and sys.argv[1] == '-v':
    verbose = True

class Handler(queue.Queue):

    def __init__(self, ws):
        queue.Queue.__init__(self)
        self.ws = ws
        self.num_workers = 5

    def add_to_queue(self, download):
        self.put(download)

    def start_workers(self):
        for i in range(self.num_workers):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()

    def isSupported(self, download):
        return True

    def start_download(self, download):
        msg = JSONer("down_" + str(download.id), 'aria2.addUri', [[download.link]])
        self.ws.send(msg)
        print("starting Download")
        startedDownloads.append(download)
        self.task_done()

    def pause_download(self, download):
        msg = JSONer("pause_" + str(download.id), 'aria2.pause', [[download.gid]])
        self.ws.send(msg)

    def worker(self):
        while True:
            download = self.get()
            if download is None or folder_size>=conf['size_limit']:
                return
            self.start_download(download)

class MessageHandler():

    def __init__(self, ws):
        self.num_workers = 5
        self.ws = ws

    def start_message_workers(self):
        for i in range(self.num_workers):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()

    def worker(self):
        global handler, folder_size, mHandler, messageQueue

        while True:
            #with get_lock:
            message = messageQueue.get()
            data = json.loads(message)
            print(threading.current_thread().name,data)
            print ("TOP LEVEL DATA", data)
            if 'error' in data:
                logging.error("Aria2c error: %s", data['error'])
                return
            if 'id' in data and data['id'] == "act":
                toBeDownloaded = get_to_download()
                if toBeDownloaded:
                    for download in toBeDownloaded:
                        handler = find_supported_handler(download)
                        if not handler:
                            handler = Handler(self.ws)
                            handlerLst.append(handler)
                        handler.add_to_queue(download)
                        print ("in download")
                        rt = RepeatedTimer(1, get_status, self.ws, download.id, None)
                    handler.join()
            elif 'id' in data:
                txt = data['id'].split('_')
                if txt[0] == "down":
                    gid = data['result']
                    db_lock.acquire()
                    set_gid(txt[1], gid)
                    set_download_gid(txt[1], gid)
                    update_status_gid(gid, Status.STARTED)
                    db_lock.release()
                elif data['id']=="stat":
                    print (data)
                    gid = data['result']['gid']
                    db_lock.acquire()
                    set_path(data['result']['gid'], data['result']['files'][0]['path'])
                    folder_size+=int(data['result']['files'][0]['completedLength'])
                    db_lock.release()
                    path=data['result']['files'][0]['path'].split('/')
                    raw_size = int(data['result']['files'][0]['length'])
                    completedLength = data['result']['files'][0]['completedLength']
                    set_name(data['result']['gid'], path[-1])
                    set_size(data['result']['gid'], raw_size)
                    download_id = get_id_from_gid(gid)
                    username = get_username_from_gid(gid)
                    send_status(download_id, completedLength, raw_size, username)
                    file_name = path[-1]
                    file_path=("/".join(path))
                    send_file_details(file_name, file_path)
                    send_details_to_minio(file_name, file_path, gid, completedLength, username, download_id, raw_size)
                    # msg='Your download '+path[-1]+' is completed.'
                    # send_mail([get_download_email(data['result']['gid'])],msg)
            elif 'method' in data:
                if data['method'] == "aria2.onDownloadComplete":
                    db_lock.acquire()
                    update_status_gid(data['params'][0]['gid'], Status.COMPLETED, True)
                    get_status(self.ws, None, data['params'][0]['gid'])
                    db_lock.release()
                    messageQueue.task_done()

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        id = self.args[1]
        if get_download_status(id) == 3:
            print ("stopping thread")
            self.stop()
        else:
            print ("run another iteration")
            self.is_running = False
            self.start()
            self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def add_uri(ws, download):
    if verbose:
        print(folder_size)
    if download is None or folder_size>=conf['size_limit']:
        return
    msg = JSONer("down_" + str(download.id), 'aria2.addUri', [[download.link]])
    ws.send(msg)

def get_status(ws, id=None, gid=None):
    if id:
        gid = get_gid_from_id(id)
    gid = str(gid)
    msg = JSONer("stat", 'aria2.tellStatus', [gid, ['gid', 'files']])
    print ("Getting status")
    ws.send(msg)


def initialize(ws):
    msg = JSONer('init', 'aria2.unpauseAll')
    ws.send(msg)
    msg = JSONer('purge', 'aria2.purgeDownloadResult')
    ws.send(msg)
    msg = JSONer('act', 'aria2.tellActive', [['gid']])
    ws.send(msg)


def JSONer(id, method, params=None):
    data = {}
    data['jsonrpc'] = '2.0'
    data['id'] = id
    data['method'] = method
    if params is not None:
        data['params'] = params
    return json.dumps(data)

def set_download_gid(id, gid):
    global startedDownloads
    for d in startedDownloads:
        if d.id == int(id):
            d.gid = gid

def send_status(id, completedLength, fileSize, username):
    progress=-1
    if fileSize>0:
        progress = int(float(completedLength)/float(fileSize) * 100)
        sc.emit('status', {'id': id, 'progress': progress}, room=username, namespace='/progress')

def find_supported_handler(download):
    for handler in handlerLst:
        if handler.isSupported(download):
            return handler
    return None


def send_file_details(file_name, file_path):
    upload_to_minio(file_name, file_path)
    logging.info("File uploaded to minio/bassa successfully !")


def send_details_to_minio(file_name, file_path, gid, completedLength, username, download_id, fileSize):
    if fileSize>0:
        update_minio_indexes(file_name, file_path, gid, completedLength, username, download_id)
        logging.info("Database table of minio updated successfully !")


def on_message(ws, message):
    global handler, folder_size, mHandler, messageQueue
    messageQueue.put(message)

def on_error(ws, error):
    logging.error(error)


def on_close(ws):
    logging.info("Socket closed")

def on_open(ws):
    initialize(ws)


def starter(socket):
    global folder_size, handler, sc, mHandler
    sc = socket
    remove_files(conf['max_age'], conf['min_rating'])
    folder_size=get_size(conf['down_folder'])
    logging.info("SERVER: folder_size: %d", folder_size)
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(conf['aria_server'],
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    handler = Handler(ws)
    handlerLst.append(handler)
    # socketio.emit("test", {'data': 'A NEW FILE WAS POSTED'}, namespace='/news')
    threading.Thread(target=handler.start_workers).start()
    mHandler = MessageHandler(ws)
    threading.Thread(target=mHandler.start_message_workers).start()
    messageQueue.join()
    ws.run_forever()



