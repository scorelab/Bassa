import logging
from worq import get_broker, TaskSpace
from pySmartDL import SmartDL




ts = TaskSpace(__name__)

def init(url):
    logging.basicConfig(filename="./debug.log", level=logging.DEBUG)
    logging.warning("INFO: Downloading Pool started ")
    broker = get_broker(url)
    broker.expose(ts)
    return broker

@ts.task
def num(value):
    return int(value)

@ts.task
def add(values):
    return values+2

@ts.task
def download(link, destination):
    logging.warning("INFO: Downloading "+link)
    obj = SmartDL(link, destination)
    obj.start(bloking=False)
    print("INFO: Download completed for "+link+" , Download file at"+obj.get_dest())