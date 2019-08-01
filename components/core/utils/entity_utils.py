from managers.DirectoryManager import Folder, File

def entity_type(e_type):
    if e_type == 'fr':
        entity_instance = Folder()
    elif e_type == 'fl':
        entity_instance = File()
    else:
        raise TypeError('No such entity exists')
    return entity_instance
