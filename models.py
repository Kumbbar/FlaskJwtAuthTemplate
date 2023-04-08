import hashlib

from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=True)


class User(db.Model):
    __tablename__ = 'users'
    salt = Config.SALT

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=True)
    surname = db.Column(db.Text, nullable=True)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Integer, unique=False, default=False)

    def check_password(self, password):
        hashed = self.hash_password(password)
        return hashed == self.password

    @classmethod
    def hash_password(cls, password):
        password = password + cls.salt
        hashed = hashlib.md5(password.encode())
        return hashed.hexdigest()