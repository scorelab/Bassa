import threading
import queue
from queue import Queue
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
mHandler = None
verbose = False
sc = None

#message handling Queue
global messageQ
messageQ = Queue()

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

####Message Handler

class MessageHandler():

    def __init__(self):
        self.num_workers = 5

    def start_message_workers(self):
        for i in range(self.num_workers):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()

    def worker(self):
        while True:
            #with get_lock:
            message = messageQ.get()
            print(threading.current_thread().name,message)
            messageQ.task_done()
            
            

#message handler

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

def on_message(ws, message):
    global handler, folder_size, mHandler, messageQ
    data = json.loads(message)
    #put messages on to the message handling queue
    messageQ.put(message)
    #mHandler.worker(ws, message)
    print ("TOP LEVEL DATA", data)
    if 'id' in data and data['id'] == "act":
        toBeDownloaded = get_to_download()
        if toBeDownloaded:
            for download in toBeDownloaded:
                handler = find_supported_handler(download)
                if not handler:
                    handler = Handler(ws)
                    handlerLst.append(handler)
                handler.add_to_queue(download)
                print ("in download")
                rt = RepeatedTimer(1, get_status, ws, download.id, None)
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
            # msg='Your download '+path[-1]+' is completed.'
            # send_mail([get_download_email(data['result']['gid'])],msg)
    elif 'method' in data:
        if data['method'] == "aria2.onDownloadComplete":
            db_lock.acquire()
            update_status_gid(data['params'][0]['gid'], Status.COMPLETED, True)
            get_status(ws, None, data['params'][0]['gid'])
            db_lock.release()


def on_error(ws, error):
    print(error)


def on_close(ws):
    pass


def on_open(ws):
    initialize(ws)


def starter(socket):
    global folder_size, handler, sc, mHandler
    sc = socket
    remove_files(conf['max_age'], conf['min_rating'])
    folder_size=get_size(conf['down_folder'])
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:6800/jsonrpc",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    handler = Handler(ws)
    # socketio.emit("test", {'data': 'A NEW FILE WAS POSTED'}, namespace='/news')
    threading.Thread(target=handler.start_workers).start()

    mHandler = MessageHandler()
    threading.Thread(target=mHandler.start_message_workers).start()
    messageQ.join()


    ws.run_forever()

########################## message Queue implementation


'''
print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(.5) # pretend to do some work.
    with print_lock:
        print(threading.current_thread().name,worker)
'''

# The threader thread pulls an worker from the queue and processes it
'''
def threader():
    while True:
        # gets an worker from the queue
        worker = messageQueue.get()

        # Run the example job with the avail worker in queue (thread)
        with print_lock:
            print(threading.current_thread().name,worker)

        # completed with the job
        messageQueue.task_done()


# how many threads are we going to allow for
for x in range(5):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()

#start = time.time()

# 20 jobs assigned.
for worker in range(20):
    messageQueue.put(worker)

# wait until the thread terminates.
messageQueue.join()

##### message queue handler##
'''


