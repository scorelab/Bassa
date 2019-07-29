"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count

def max_workers():
    return 2*cpu_count()+1

bind = '0.0.0.0:5000'
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()
threads= 2
