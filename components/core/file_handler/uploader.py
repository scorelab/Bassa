import os
import cgi
import cgitb
import shutil
from ConfReader import get_conf_reader

cgitb.enable()
conf = get_conf_reader("up.conf")
UPLOAD_DIR = conf['upload_folder']

headers = {
    'Host': 'localhost:5000',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://localhost:3000',
}

def upload_file_helper(file_field):
    response = dict()
    try:
        file_form = cgi.FieldStorage()
        if file_field not in file_form:
            response['msg'] = 'Invalid input'
            return response

        file_content = file_form[file_field]
        if not file_content.file:
            response['msg'] = 'No file found'
            return response

        path = os.path.join(UPLOAD_DIR, file_content.filename)

        with open(path, 'wb') as file_out:
            shutil.copyfileobj(file_content.file, file_out, conf['size_limit'])

        response['msg'] = 'success'
        response['name'] = str(file_content.filename)
        return response

    except Exception as e:
        response['err'] = str(e)
        return response