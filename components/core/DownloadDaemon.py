import threading
import queue
import json, time
from DownloadManager import *
from Models import Status, Download
from EMail import send_mail
from DiskMan import *
from ConfReader import get_conf_reader

import websocket
import sys


conf = get_conf_reader("dl.conf")
db_lock = threading.Lock()
folder_size=0
startedDownloads = []
handlerLst = []
handler = None
verbose = False

if len(sys.argv) == 2 and sys.argv[1] == '-v':
    verbose = True

class Handler(queue.Queue):

    def __init__(self, ws):
        queue.Queue.__init__(self)
        self.ws = ws
        self.num_workers = 5
        self.start_workers()

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

def add_uri(ws, download):
    if verbose:
        print(folder_size)
    if download is None or folder_size>=conf['size_limit']:
        return
    msg = JSONer("down_" + str(download.id), 'aria2.addUri', [[download.link]])
    ws.send(msg)

def get_status(ws, gid):
    msg = JSONer("stat", 'aria2.tellStatus', [gid, ['gid', 'files']])
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

def findSupportedHandler(download):
    for handler in handlerLst:
        if handler.isSupported(download):
            return handler
    return None

def on_message(ws, message):
    global handler
    data = json.loads(message)
    if 'id' in data and data['id'] == "act":
        toBeDownloaded = get_to_download()
        for download in toBeDownloaded:
            handler = findSupportedHandler(download)
            if not handler:
                handler = Handler(ws)
                handlerLst.append(handler)
            handler.add_to_queue(download)
        handler.join()
    elif 'id' in data:
        txt = data['id'].split('_')
        if txt[0] == "down":
            db_lock.acquire()
            set_gid(txt[1], data['result'])
            set_download_gid(txt[1], data['result'])
            update_status_gid(data['result'], Status.STARTED)
            db_lock.release()
        elif data['id']=="stat":
            db_lock.acquire()
            set_path(data['result']['gid'], data['result']['files'][0]['path'])
            folder_size+=int(data['result']['files'][0]['completedLength'])
            db_lock.release()
            path=data['result']['files'][0]['path'].split('/')
            msg='Your download '+path[-1]+' is completed.'
            # send_mail([get_download_email(data['result']['gid'])],msg)
    elif 'method' in data:
        if data['method'] == "aria2.onDownloadComplete":
            db_lock.acquire()
            update_status_gid(data['params'][0]['gid'], Status.COMPLETED, True)
            get_status(ws, data['params'][0]['gid'])
            add_uri(ws, get_to_download())
            db_lock.release()


def on_error(ws, error):
    print(error)


def on_close(ws):
    pass


def on_open(ws):
    initialize(ws)


def starter():
    global folder_size, handler
    # remove_files(conf['max_age'], conf['min_rating'])
    folder_size=get_size(conf['down_folder'])
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:6800/jsonrpc",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    handler = Handler(ws)
    threading.Thread(target=handler.start_workers).start()

    ws.run_forever()
