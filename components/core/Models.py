class User:
    def __init__(self, id, userName, password, auth, email):
        self.id=id
        self.userName=userName
        self.password=password
        self.auth=auth
        self.email=email

class AuthLeval:
    ADMIN, STUDENT, ACADEMIC, NONACADEMIC= list(range(4))

class Workspace:
    def __init__(self, id, name, user_id):
        self.id=id
        self.name=name
        self.user_id=user_id

class Project:
    def __init__(self, id, name, workspace_id):
        self.id=id
        self.name=name
        self.workspace_id=workspace_id

class Folder:
    def __init__(self, id, name, workspace_id, project_id, folder_id):
        self.id=id
        self.name=name
        self.workspace_id=workspace_id
        self.project_id=project_id
        self.folder_id=folder_id

class File:
    def __init__(self, id, name, project_id, folder_id):
        self.id=id
        self.name=name
        self.project_id=project_id
        self.folder_id=folder_id

class ACL:
    def __init__(self, user_id, file_id, folder_id, permissions):
        self.user_id=user_id
        self.folder_id=folder_id
        self.file_id-file_id
        self.permissions=permissions

class Download:
    def __init__(self, link, userName, id=None):
        self.link=link
        self.userName=userName
        self.id=id
        self.gid=None
    def __str__(self):
        return "id: %s, user: %s, link: %s, gid: %s" % (self.id, self.userName, self.link, self.gid)

class Status:

    DEFAULT, STARTED, DELETED, COMPLETED, ERROR= list(range(5))
