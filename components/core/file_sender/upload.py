import os
import cgi
import cgitb
import shutil
from ConfReader import get_conf_reader

cgitb.enable()
conf = get_conf_reader("dl.conf")
UPLOAD_DIR = conf['upload_folder']


def upload_file(file_field):
    file_form = cgi.FieldStorage()
    if file_field not in file_form:
        return 'Invalid input'

    file_content = file_form[file_field]
    if not file_content.file:
        return 'No file found'

    path = os.path.join(UPLOAD_DIR, file_content.filename)
    with open(path, 'wb') as file_out:
        shutil.copyfileobj(file_content.file, file_out, conf['size_limit'])
