from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import yaml
import os

configs = ''
path = ''


def retreive_values():
    global path
    global configs
    path = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
    stream = open(path+"/bassa.yml", "r")
    configs = yaml.safe_load(stream)


retreive_values()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = configs['database']['database_type']+':/'+configs['database']['database_user_username']+':'+configs['database']['database_user_password']+'@'+configs['database']['database_ip']+'/'+configs['database']['database_name']

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class user(db.Model):
    __tablename__ = 'user'
    user_name = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    auth = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(256), nullable=False)
    blocked = db.Column(db.Integer, nullable=False, default=0)
    approved = db.Column(db.Integer, nullable=False, default=0)


class download(db.Model):
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


class rate(db.Model):
    __tablename__ = 'rate'
    user_name = db.Column(db.String(256), nullable=False)
    id = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)

if __name__ == '__main__':
    manager.run()

