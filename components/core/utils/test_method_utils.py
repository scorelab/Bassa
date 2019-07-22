from managers.DirectoryManager import Folder, File


def username():
    return 'admin'

def password():
    return 'admin'

def usernamer():
    return 'rand'

def passwordr():
    return 'pass'

def user_id():
    return '2'

def access_id():
    return '1'

def access_user():
    return 'rush'

def folder():
    return 'fr'

def file():
    return 'fl'

def access():
    return 'write'

def folder_instance():
    return Folder()

def file_instance():
    return File()


def entity_name(param):
    if param == 'add':
        return 'test_entity'
    else:
        return 'edit_test_entity'


def parent_id():
    return '0'

def entity_id():
     # subject to change
     return '4'