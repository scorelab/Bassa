import thread
import json, inspect, os, time
from DownloadManager import *
from Models import Status

import websocket

conf={}

def conf_reader () :
    global conf
    file=open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"/dl.conf")
    txt=""
    for line in file:
       txt+=line.strip()
    conf=json.loads(txt)

def add_uri(ws, download):
    if download is None:
        return
    msg=JSONer("down_"+str(download.id), 'aria2.addUri', [[download.link]])
    ws.send(msg)


def queue_adder(ws, num):
    for i in range(0,num):
        add_uri(ws, get_to_download())
        time.sleep(2)


def message_handle(ws, message):
    print message
    data=json.loads(message)
    if 'id' in data and data['id']=="act":
        remain=conf['max_downloads']-len(data['result'])
        if remain>0:
            queue_adder(ws, remain)
    elif 'id' in data:
        txt=data['id'].split('_')
        if txt[0]=="down":
            set_gid(txt[1], data['result'])
            update_status_gid(data['result'], Status.STARTED)
    elif 'method' in data:
        if data['method']=="aria2.onDownloadComplete":
            update_status_gid(data['params'][0]['gid'], Status.COMPLETED, True)
            add_uri(ws, get_to_download())
        # if data['method']=="aria2.onDownloadStart":
        #     update_status_gid(data['params'][0]['gid'], Status.STARTED)

def initialize (ws):
    msg=JSONer('init', 'aria2.unpauseAll')
    ws.send(msg)
    msg=JSONer('act','aria2.tellActive', [['gid']])
    ws.send(msg)

def JSONer (id, method, params=None):
    data = {}
    data['jsonrpc'] = '2.0'
    data['id'] = id
    data['method'] = method
    if params is not None:
        data['params'] = params
    return  json.dumps(data)

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
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()
