import os
from ConfReader import get_conf_reader

conf = get_conf_reader("up.conf")
UPLOAD_DIR = conf['upload_folder']


def upload_file_helper(file_data):
    response = dict()
    try:
        if not file_data:
            response['msg'] = 'No file found'
            return response

        name,ext = os.path.splitext(file_data.filename)
        f_name = name + ext
        upload_path = os.path.join(UPLOAD_DIR, f_name)
        file_data.save(upload_path)

        response['msg'] = 'success'
        response['name'] = f_name
        response['path'] = upload_path
        response['ext'] = ext
        return response

    except Exception as e:
        response['err'] = str(e)
        return response