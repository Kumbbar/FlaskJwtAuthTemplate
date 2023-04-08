import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from services.users import get_all_users, get_user_data_dict, get_user_by_id,get_user_data_json
from flask import Response

users = Blueprint('users', __name__)


def admin_required(func):
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            return Response(
                json.dumps({'error': 'Admin user required'}),
                status=400,
                mimetype='application/json'
            )
        result = func(*args, **kwargs)
        return result
    wrapper.__name__ = func.__name__
    return wrapper


@users.route('/all', methods=['GET'])
@jwt_required()
@admin_required
def get_users():
    users = get_all_users()
    result = []
    for user in users:
        result.append(get_user_data_dict(user))
    return Response(json.dumps(result), status=200, mimetype='application/json')


@users.route('/', methods=['GET'])
@jwt_required()
def get_user():
    user_id = request.json.get("id", None)
    if user_id:
        user = get_user_by_id(id)
        return get_user_data_json(user)
    return Response(json.dumps({'error': 'User_id required'}, status=400, mimetype='application/json'))


@users.route('/', methods=['GET'])
@except_validation_error_decorator
def edit_object() -> Response:
    """Edit object longitude and latitude in database by title from json request"""
    target_object = request.json
    title, longitude, latitude = check_edit_request(target_object)

    modified_object = Object.select().where(Object.title == title).get()
    modified_object.longitude = longitude
    modified_object.latitude = latitude
    modified_object.save()
    return Response(json.dumps(target_object), status=200, mimetype='application/json')