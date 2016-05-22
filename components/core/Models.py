class User:
    def __init__(self, userName, password, auth, email):
        self.userName=userName
        self.password=password
        self.auth=auth
        self.email=email

class AuthLeval:
    ADMIN, STUDENT, ACADEMIC, NONACADEMIC= list(range(4))

class Download:
    def __init__(self, link, userName, id):
        self.link=link
        self.userName=userName
        self.id=id
        self.gid=None

class Status:

    DEFAULT, STARTED, DELETED, COMPLETED, ERROR= list(range(5))