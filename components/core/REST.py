from flask import Flask
from flask import request
from worq import get_queue
from redis import Redis
from rq import Queue
from func import downloadMe

server = Flask(__name__)
q = get_queue("memory://")
redis_conn = Redis()
qu = Queue(connection=redis_conn)

@server.route('/')
def index():
    return "Bassa 2"

@server.route('/api/download',  methods=['GET'])
def download():
    link = request.args.get('link', '')
    destination = "~/Desktop/"
    #r = q.tasks.add(2)
    #print(r)
    q.tasks.download(link, destination)
    return '{ "msg": "Added to the queue"}'

@server.route('/api/download1',  methods=['GET'])
def download1():
    link = request.args.get('link', '')
    job = qu.enqueue(downloadMe,link)
    return '{ "msg": "Added to the queue"}'
