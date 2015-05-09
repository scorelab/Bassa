import sys
from worq.pool.process import WorkerPool
from Works import init

def start_worker():
    broker = init("memory://")
    pool = WorkerPool(broker, init, workers=2)
    print("Pool starting")
    pool.start(handle_sigterm=False)
    return pool