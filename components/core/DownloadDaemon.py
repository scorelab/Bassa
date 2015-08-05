import thread
import json, inspect, os, time
from DownloadManager import *
from Models import Status
from EMail import send_mail

import websocket

conf = {}
db_lock = thread.allocate_lock()

def conf_reader():
    global conf
    file = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/dl.conf")
    txt = ""
    for line in file:
        txt += line.strip()
    conf = json.loads(txt)


def add_uri(ws, download):
    if download is None:
        return
    msg = JSONer("down_" + str(download.id), 'aria2.addUri', [[download.link]])
    ws.send(msg)

def get_status(ws, gid):
    msg = JSONer("stat", 'aria2.tellStatus', [gid, ['gid', 'files']])
    ws.send(msg)

def queue_adder(ws, num):
    for i in range(0, num):
        add_uri(ws, get_to_download())
        time.sleep(2)


def message_handle(ws, message):
    print message
    data = json.loads(message)
    if 'id' in data and data['id'] == "act":
        remain = conf['max_downloads'] - len(data['result'])
        if remain > 0:
            queue_adder(ws, remain)
    elif 'id' in data:
        txt = data['id'].split('_')
        if txt[0] == "down":
            db_lock.acquire()
            set_gid(txt[1], data['result'])
            update_status_gid(data['result'], Status.STARTED)
            db_lock.release()
        elif data['id']=="stat":
            db_lock.acquire()
            set_path(data['result']['gid'], data['result']['files'][0]['path'])
            db_lock.release()
            path=data['result']['files'][0]['path'].split('/')
            msg='Your download '+path[-1]+' is completed.'
            send_mail([get_download_email(data['result']['gid'])],msg)
    elif 'method' in data:
        if data['method'] == "aria2.onDownloadComplete":
            db_lock.acquire()
            update_status_gid(data['params'][0]['gid'], Status.COMPLETED, True)
            get_status(ws, data['params'][0]['gid'])
            add_uri(ws, get_to_download())
            db_lock.release()
        # elif data['method'] == "aria2.onDownloadError":
        #     get_status(ws, data['params'][0]['gid'])


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


def on_message(ws, message):
    thread.start_new_thread(message_handle, (ws, message))


def on_error(ws, error):
    print error


def on_close(ws):
    pass


def on_open(ws):
    initialize(ws)


def starter():
    conf_reader()
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:6800/jsonrpc",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()
