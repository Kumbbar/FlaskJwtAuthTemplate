from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required

from services.users import get_user_by_id
from config import Config
from datetime import timedelta

jwt = JWTManager()


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    if hasattr(user, 'id'):
        return user.id
    return user


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]  # user_id
    return get_user_by_id(identity)


def create_user_tokens(user):
    access_token = create_access_token(identity=user, expires_delta=timedelta(hours=Config.ACCESS_TOKEN_TTL))
    refresh_token = create_refresh_token(identity=user, expires_delta=timedelta(days=Config.REFRESH_TOKEN_TTL))
    return access_token, refresh_token


def create_user_access_token(identity):
    return create_access_token(identity=identity, fresh=False)