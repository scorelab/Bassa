from initializer import server, socketio
from flask import send_file, send_from_directory
from flask_socketio import join_room
import os
from file_handler import sender
from routes import User, Download, Directory, Acl, Upload


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


# download endpoints
server.add_url_rule(rule='/download/start', endpoint='start', view_func=Download.start)
server.add_url_rule(rule='/download/kill', endpoint='kill', view_func=Download.kill)
server.add_url_rule(rule='/api/download', endpoint='add_download_request', view_func=Download.add_download_request,
					methods=['POST'])
server.add_url_rule(rule='/api/download/<int:id>', endpoint='remove_download_request',
					view_func=Download.remove_download_request, methods=['DELETE'])
server.add_url_rule(rule='/api/download/rate/<int:id>', endpoint='rate_download_request',
					view_func=Download.rate_download_request, methods=['POST'])
server.add_url_rule(rule='/api/downloads/<int:limit>', endpoint='get_downloads_request',
					view_func=Download.get_downloads_request, methods=['GET'])
server.add_url_rule(rule='/api/download/<int:id>', endpoint='get_download', view_func=Download.get_download,
					methods=['GET'])

# user action api endpoints
server.add_url_rule(rule='/api/login', endpoint='login', view_func=User.login, methods=['POST'])
server.add_url_rule(rule='/api/regularuser', endpoint='regular_user_request', view_func=User.regular_user_request,
					methods=['POST'])
server.add_url_rule(rule='/api/user', endpoint='add_user_request', view_func=User.add_user_request, methods=['POST'])
server.add_url_rule(rule='/api/user/<string:username>', endpoint='remove_user_request',
					view_func=User.remove_user_request, methods=['DELETE'])
server.add_url_rule(rule='/api/user/<string:username>', endpoint='update_user_request',
					view_func=User.update_user_request, methods=['PUT'])
server.add_url_rule(rule='/api/user', endpoint='get_users_request', view_func=User.get_users_request, methods=['GET'])
server.add_url_rule(rule='/api/user/requests', endpoint='get_user_signup_requests',
					view_func=User.get_user_signup_requests, methods=['GET'])
server.add_url_rule(rule='/api/user/approve/<string:username>', endpoint='approve_user_request',
					view_func=User.approve_user_request, methods=['POST'])
server.add_url_rule(rule='/api/user/blocked', endpoint='get_blocked_users_request',
					view_func=User.get_blocked_users_request, methods=['GET'])
server.add_url_rule(rule='/api/user/blocked/<string:username>', endpoint='block_user_request',
					view_func=User.block_user_request, methods=['POST'])
server.add_url_rule(rule='/api/user/blocked/<string:username>', endpoint='unblock_user_request',
					view_func=User.unblock_user_request, methods=['DELETE'])
server.add_url_rule(rule='/api/user/downloads/<int:limit>', endpoint='get_downloads_user_request',
					view_func=User.get_downloads_user_request, methods=['GET'])
server.add_url_rule(rule='/api/user/heavy', endpoint='get_topten_heaviest_users',
					view_func=User.get_topten_heaviest_users, methods=['GET'])

# file sending endpoints
server.add_url_rule(rule='/api/file', endpoint='send_file_from_path', view_func=sender.send_file_from_path, methods=['GET'])
server.add_url_rule(rule='/api/compress', endpoint='start_compression', view_func=sender.start_compression, methods=['POST'])
server.add_url_rule(rule='/api/compression-progress', endpoint='get_compression_progress', view_func=sender.check_compression_progress, methods=['GET'])


# storage entity endpoints
server.add_url_rule(rule='/api/user/<string:user_id>/drive/<string:id>/children', endpoint='fetch_entity_children',
					view_func=Directory.fetch_entity_children, methods=['GET'])
server.add_url_rule(rule='/api/user/<string:user_id>/drive/<string:id>', endpoint='fetch_entity',
					view_func=Directory.fetch_entity, methods=['GET'])
server.add_url_rule(rule='/api/user/<string:user_id>/drive/<string:id>/move', endpoint='move_entity',
					view_func=Directory.move_entity, methods=['POST'])
server.add_url_rule(rule='/api/user/<string:user_id>/drive/<string:id>/add', endpoint='add_entity',
					view_func=Directory.add_entity, methods=['POST'])
server.add_url_rule(rule='/api/user/<string:user_id>/drive/<string:id>/edit', endpoint='edit_entity',
					view_func=Directory.edit_entity, methods=['PUT'])
server.add_url_rule(rule='/api/user/<string:user_id>/drive/<string:id>/remove', endpoint='remove_entity',
					view_func=Directory.remove_entity, methods=['DELETE'])

# acl endpoints
server.add_url_rule(rule='/api/user/<string:user_id>/drive/<string:id>/check', endpoint='check_access',
					view_func=Acl.check_access, methods=['GET'])
server.add_url_rule(rule='/api/user/<string:user_id>/drive/shared', endpoint='get_shared_entities',
					view_func=Acl.get_shared_entities, methods=['GET'])
server.add_url_rule(rule='/api/user/drive/<string:id>/grant', endpoint='grant_access',
					view_func=Acl.grant_access, methods=['POST'])

# file uploading endpoints
server.add_url_rule(rule='/api/user/drive/<string:user_id>/upload', endpoint='upload_file_to_server',
					view_func=Upload.upload_file_to_server, methods=['POST'])
