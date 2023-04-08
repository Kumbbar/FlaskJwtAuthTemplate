from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from services.users import get_users

users = Blueprint('users', __name__)


@users.route('/', methods=['GET'])
def get_users():
    pass



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