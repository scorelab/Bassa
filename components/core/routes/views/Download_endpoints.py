from flask import Blueprint
from routes.Download import *

downloadprint = Blueprint("download", __name__)

downloadprint.add_url_rule(rule='/api/download/start',
                           endpoint='start',
                           view_func=start)

downloadprint.add_url_rule(rule='/api/download/kill',
                           endpoint='kill',
                           view_func=kill)

downloadprint.add_url_rule(rule='/api/download',
                           endpoint='add_download_request',
                           view_func=add_download_request,
                           methods=['POST'])

downloadprint.add_url_rule(rule='/api/download/<int:id>',
                           endpoint='remove_download_request',
                           view_func=remove_download_request,
                           methods=['DELETE'])

downloadprint.add_url_rule(rule='/api/download/rate/<int:id>',
                           endpoint='rate_download_request',
                           view_func=rate_download_request,
                           methods=['POST'])

downloadprint.add_url_rule(rule='/api/downloads/<int:limit>',
                           endpoint='get_downloads_request',
                           view_func=get_downloads_request,
                           methods=['GET'])

downloadprint.add_url_rule(rule='/api/download/<int:id>',
                           endpoint='get_download',
                           view_func=get_download,
                           methods=['GET'])

downloadprint.add_url_rule(rule='/api/file_from_minio/<int:id>',
                           endpoint='get_file_from_minio',
                           view_func=get_file_from_minio,
                           methods=['GET'])
