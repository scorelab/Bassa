class User:
    def __init__(self, userName, password, auth, email):
        self.userName=userName
        self.password=password
        self.auth=auth
        self.email=email

class AuthLeval:
    ADMIN, STUDENT, ACADEMIC, NONACADEMIC= list(range(4))

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
