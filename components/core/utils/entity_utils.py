from managers.DirectoryManager import Folder, File

def entity_type(type):
    if type == 'fr':
        instance = Folder()
    elif type == 'fl':
        instance = File()
    else:
        raise TypeError('No such entity exists')
    return instance