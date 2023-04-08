import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from services.users import get_all_users, get_user_data_dict, get_user_by_id,get_user_data_json
from flask import Response

from models import User, db

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
@admin_required
def get_user():
    user_id = request.json.get("id", None)
    if user_id:
        user = get_user_by_id(id)
        return get_user_data_json(user)
    return Response(json.dumps({'error': 'User_id required'}, status=400, mimetype='application/json'))


@users.route('/', methods=['PUT'])
@jwt_required()
@admin_required
def edit_user():
    user_id = request.json.get("id", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(id=user_id).update(request.json)
    if password:
        get_user_by_id(user_id).password = User.hash_password(password)
    db.session.commit()
    return Response(json.dumps({'success': 'user_updated'}), status=200, mimetype='application/json')


@users.route('/', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user():
    user_id = request.json.get("id", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(id=user_id).update(request.json)
    if password:
        get_user_by_id(user_id).password = User.hash_password(password)
    db.session.commit()
    return Response(json.dumps({'success': 'user_updated'}), status=200, mimetype='application/json')
