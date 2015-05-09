from flask import Flask
from flask import request
from worq import get_queue


server = Flask(__name__)
q = get_queue("memory://")


@server.route('/')
def index():
    return "Bassa 2"

@server.route('/api/download',  methods=['GET'])
def download():
    link = request.args.get('link', '')
    destination = "~/Desktop/"
    r = q.tasks.add(2)
    print(r)
    #q.tasks.download(link, destination)
    return '{ "msg": "Added to the queue"}'