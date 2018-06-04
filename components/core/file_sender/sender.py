from Server import *
from flask import Response
from Main import logging


@server.route("/api/get/file", methods=['GET'])
def send_file_from_path():
    # TODO :: Add Authorization to the request
    try:
        gid = request.args.get('gid')
        logging.info('User asked for file, having GID ' + gid)
        id = get_id_from_gid(gid)
        download_path = get_download_path(id)
        download_name = get_download_name_from_id(id)
    except Exception as e:
        logging.error(" get file API (/api/get/file) got wrong arguments, thrown an error :: %s" % e)
        return Response("error", status=200)

    try:
        return send_file(filename_or_fp=download_path, attachment_filename=download_name,
                         as_attachment=True)
    except Exception as e:
        logging.error("File sending has a exception. We got :: %s on file sending" % e)
        return Response("File you are trying to access is not available to us. Please ask admin to check the server",
                        status=200)
