from flask import jsonify
from models import User, Role


def get_role_data_dict(role):
    return dict(
        id=role.id,
        title=role.title,
    )


def get_role_data_json(role):
    return jsonify(
        id=role.id,
        title=role.title
    )


def get_role_by_id(user_id: int) -> (User, None):
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