import json

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from services.roles import get_all_roles
from flask import Response

from models import User, db, Role
from .decorators import admin_required
from services.roles import get_all_roles, get_role_data_dict, get_role_by_id, get_role_data_json

roles = Blueprint('roles', __name__)


@roles.route('/all', methods=['GET'])
@jwt_required()
@admin_required
def get_roles():
    roles = get_all_roles()
    result = []
    for role in roles:
        result.append(get_role_data_dict(role))
    return Response(json.dumps(result), status=200, mimetype='application/json')


@roles.route('/one', methods=['POST'])
@jwt_required()
@admin_required
def get_role():
    role_id = request.json.get("id", None)
    if role_id:
        role = get_role_by_id(role_id)
        return get_role_data_json(role)
    return Response(json.dumps({'error': 'id required'}, status=400, mimetype='application/json'))


@roles.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_role():
    password = request.json.get('password', None)
    email = request.json.get('password', None)

    role = Role(**request.json)
    db.session.add(role)
    db.session.commit()
    return Response(json.dumps({'success': 'role created'}), status=200, mimetype='application/json')


@roles.route('/', methods=['PUT'])
@jwt_required()
@admin_required
def edit_role():
    role_id = request.json.get("id", None)
    user = Role.query.filter_by(id=role_id).update(request.json)
    db.session.commit()
    return Response(json.dumps({'success': 'role updated'}), status=200, mimetype='application/json')


@roles.route('/', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user():
    role_id = request.json.get("id", None)
    role = get_role_by_id(role_id)
    db.session.delete(role)
    db.session.commit()
    return Response(json.dumps({'success': 'role deleted'}), status=200, mimetype='application/json')
