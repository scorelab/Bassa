import os
import time
import sys
from DownloadManager import get_to_delete, set_delete_status
import logging

SECS_PER_DAY=86400
verbose = False

if len(sys.argv) == 2 and sys.argv[1] == '-v':
    verbose = True

def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def remove_files(days, rate):
    time_now=int(time.time())
    time_then=time_now-(days*SECS_PER_DAY)
    files=get_to_delete(time_then, rate)
    if verbose:
        print("files to be removed", files)
    for file in files:
        try:
            os.unlink(file[0])
        except FileNotFoundError:
            logging.error('Following file was not found on this path :: %s , removing the match from the database' %
                          file[0])
        set_delete_status(file[0])