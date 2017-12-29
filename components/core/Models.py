class User:
    __tablename__ = 'User'
    user_name = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    auth = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(256), nullable=False)
    blocked = db.Column(db.Integer, nullable=False, default=0)
    approved = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, userName, password, auth, email):
        self.userName=userName
        self.password=password
        self.auth=auth
        self.email=email

class AuthLeval:
    ADMIN, STUDENT, ACADEMIC, NONACADEMIC= list(range(4))

class Download:
    __tablename__ = 'download'
    id = db.Column(db.Integer, nullable=False)
    link = db.Column(db.Text, nullable=False)
    user_name = db.Column(db.String(256), nullable=False)
    download_name = db.Column(db.String(256), nullable=False)
    added_time = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    rating = db.Column(db.Integer, nullable=False, default=0)
    gid = db.Column(db.String(256), nullable=False)
    completed_time = db.Column(db.Integer, nullable=False, default=0)
    size = db.Column(db.String(7), nullable=False, default=0)
    path = db.Column(db.Text)

    def __init__(self, link, userName, id=None):
        self.link=link
        self.userName=userName
        self.id=id
        self.gid=None
    def __str__(self):
        return "id: %s, user: %s, link: %s, gid: %s" % (self.id, self.userName, self.link, self.gid)

class Rate: 
    __tablename__ = 'rate'
    user_name = db.Column(db.String(256), nullable=False)
    id = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)

    def __init__(self, user_name, id, rate):
        self.user_name=user_name
        self.id=id
        self.rate=rate

class Status:
    DEFAULT, STARTED, DELETED, COMPLETED, ERROR= list(range(5))
