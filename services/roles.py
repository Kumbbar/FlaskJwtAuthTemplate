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




def get_all_roles():
    return Role.query.all()