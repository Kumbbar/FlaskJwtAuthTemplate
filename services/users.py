from flask import jsonify
from models import User, Role


def get_user_data_dict(user):
    return dict(
        id=user.id,
        email=user.email,
        name=user.name,
        surname=user.surname,
        role=user.role
    )


def get_user_data_json(user):
    return jsonify(
        id=user.id,
        email=user.email,
        name=user.name,
        surname=user.surname,
        role=user.role
    )


def get_user_by_email(email:str) -> (User, None):
    return User.query.filter_by(email=email).one_or_none()


def get_user_by_id(user_id: int) -> (User, None):
    return User.query.filter_by(id=user_id).one_or_none()


def create_user(email, password, name=None, surname=None):
    user = User(
        email=email,
        password=User.hash_password(password),
        name=name,
        surname=surname,
    )
    return user


def get_all_users():
    return User.query.all()