import os
import time
from DownloadManager import get_to_delete, set_delete_status

SECS_PER_DAY=86400

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
    print("files to be removed", files)
    for file in files:
        print(file[0])
        os.unlink(file[0])
        set_delete_status(file[0])