from flask import Flask
from flask import request
from pySmartDL import SmartDL


server = Flask(__name__)


@server.route('/')
def index():
    return "Bassa"

@server.route('/api/download',  methods=['GET'])
def download():
    link = request.args.get('link', '')
    destination = "./dl"
    obj = SmartDL(link, destination)
    obj.start()
    return obj.get_dest()
