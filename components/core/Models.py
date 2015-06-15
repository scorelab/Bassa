class User:
    def __init__(self, userName, password, auth, email):
        self.userName=userName
        self.password=password
        self.auth=auth
        self.email=email

class AuthLeval:

    ADMIN, STUDENT, ACADEMIC, NONACADEMIC= range(4)
