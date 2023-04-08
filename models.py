import hashlib

from flask_sqlalchemy import SQLAlchemy

from config import Config


db = SQLAlchemy()


# USERS

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
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), default=1)
    is_admin = db.Column(db.Integer, unique=False, default=False)

    def check_password(self, password):
        hashed = self.hash_password(password)
        return hashed == self.password

    @classmethod
    def hash_password(cls, password):
        password = password + cls.salt
        hashed = hashlib.md5(password.encode())
        return hashed.hexdigest()


# PURCHASES


class ProductCategory(db.Model):
    __tablename__ = 'products_categories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=True)


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    category = db.Column(db.Integer, db.ForeignKey('products_categories.id'), nullable=True)


# class Purchase(db.Model):
#     __tablename__ = 'products'
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.Text, nullable=False, unique=True)
#     category = db.relationship(ProductCategories, backref='products_categories')


# CAFE
# class Cafe(db.Model):
#     __tablename__ = 'cafes'
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.Text, nullable=True, unique=False)
#     address = db.Column(db.Text, nullable=False, unique=True)
#     longitude = db.Column(db.Decimal(3, 10), nullable=True)
#     latitude = db.Column(db.Decimal(3, 10), nullable=True)


# Provide

class Provider(db.Model):
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, unique=False)


