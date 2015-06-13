from flask import Flask
from flask import request
from redis import Redis
from rq import Queue
from func import downloadMe

server = Flask(__name__)
redis_conn = Redis()
qu = Queue(connection=redis_conn)


@server.route('/')
def index():
    return "Bassa 2"


@server.route('/api/download',  methods=['GET'])
def download():
    link = request.args.get('link', '')
    job = qu.enqueue(downloadMe, link)
    return '{ "msg": "Added to the queue"}'
