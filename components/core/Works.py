import logging
from worq import get_broker, TaskSpace
from pySmartDL import SmartDL

ts = TaskSpace(__name__)

def init(url):
    logging.basicConfig(level=logging.DEBUG)
    broker = get_broker(url)
    broker.expose(ts)
    return broker

@ts.task
def num(value):
    return int(value)

@ts.task
def add(values):
    return values+2;

@ts.task
def download(link, destination):
    print("INFO: Downloading "+link)
    obj = SmartDL(link, destination)
    obj.start()
    print("INFO: Download completed for "+link+" , Download file at"+obj.get_dest())