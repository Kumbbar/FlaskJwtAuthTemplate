import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from services.users import get_all_users, get_user_data_dict
from flask import Response

users = Blueprint('users', __name__)


def admin_required(func):
    def wrapper():
        pass

    wrapper.__name__ = func.__name__
    return wrapper


@users.route('/all', methods=['GET'])
def get_users():
    users = get_all_users()
    result = []
    for user in users:
        result.append(get_user_data_dict(user))
    return Response(json.dumps(result), status=200, mimetype='application/json')


# @app.route('/objects/edit', methods=['POST'])
# @except_validation_error_decorator
# def edit_object() -> Response:
#     """Edit object longitude and latitude in database by title from json request"""
#     target_object = request.json
#     title, longitude, latitude = check_edit_request(target_object)
#
#     modified_object = Object.select().where(Object.title == title).get()
#     modified_object.longitude = longitude
#     modified_object.latitude = latitude
#     modified_object.save()
#     return Response(json.dumps(target_object), status=200, mimetype='application/json')