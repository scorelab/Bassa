from initializer import server, socketio
from flask import send_file, send_from_directory
from flask_socketio import join_room
import os
from file_sender import sender
from routes.views import User_endpoints, Download_endpoints, FileSender_endpoints


# socket connections
@socketio.on('join', namespace='/progress')
def on_join(data):
	room = data['room']
	if room != '':
		join_room(room)


# endpoints

@server.route('/ui/<string:path>')
def serve_ui(path):
	return send_from_directory(os.path.dirname(os.path.realpath(__file__)) + "/ui", path)


@server.route('/ui/')
def serve_ui1():
	return send_file(os.path.dirname(os.path.realpath(__file__)) + "/ui/index.html")



def register_blueprint(server):
    """Register Flask blueprints."""
    server.register_blueprint(User_endpoints.userprint, url_prefix="/api")
    server.register_blueprint(Download_endpoints.downloadprint)
    server.register_blueprint(FileSender_endpoints.filesenderprint, url_prefix="/api")
    return None
