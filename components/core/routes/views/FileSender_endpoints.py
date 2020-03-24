from flask import Blueprint
from file_sender.sender import *

filesenderprint = Blueprint("filesenderprint", __name__)

filesenderprint.add_url_rule(rule='/file',
                        endpoint='send_file_from_path',
                        view_func=send_file_from_path,
                        methods=['GET'])

filesenderprint.add_url_rule(rule='/compress',
                        endpoint='start_compression',
                        view_func=start_compression,
                        methods=['POST'])

filesenderprint.add_url_rule(rule='/compression-progress',
                        endpoint='get_compression_progress',
                        view_func=check_compression_progress,
                        methods=['GET'])
