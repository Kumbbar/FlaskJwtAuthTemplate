import hashlib

from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


class User(db.Model):
    salt = Config.SALT

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def check_password(self, password):
        hashed = self.hash_password(password)
        return hashed == self.password

    @classmethod
    def hash_password(cls, password):
        password = password + cls.salt
        hashed = hashlib.md5(password.encode())
        return hashed.hexdigest()