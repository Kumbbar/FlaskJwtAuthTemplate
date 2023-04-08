from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity

from .jwt_auth import create_user_access_token, create_user_tokens
from models import db
from services.users import create_user, get_user_by_email, get_user_data_json


auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = get_user_by_email(email)
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401

    access_token, refresh_token = create_user_tokens(user)
    return jsonify(access_token=access_token, refresh_token=refresh_token)


@auth.route("/register", methods=["POST"])
def register():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    name = request.json.get("name", None)
    surname = request.json.get("surname", None)

    if get_user_by_email(email):
        return jsonify(error="User with this email already exists"), 400
    user = create_user(email=email, password=password, name=name, surname=surname)
    db.session.add(user)
    db.session.commit()

    access_token, refresh_token = create_user_tokens(user)
    return jsonify(access_token=access_token, refresh_token=refresh_token)


@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_tokens():
    identity = get_jwt_identity()
    access_token = create_user_access_token(identity=identity)
    return jsonify(access_token=access_token)


@auth.route("/profile", methods=["GET"])
@jwt_required()
def get_user_data():
    return get_user_data_json(current_user)