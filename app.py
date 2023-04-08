import os

from flask import Flask
from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user

from config import config_dict
from models import db
from apps.auth.auth import auth
from apps.users.roles import roles
from apps.users.users import users
from apps.products.products import products
from apps.auth.jwt_auth import jwt, create_user_access_token, create_user_tokens
from services.users import get_user_by_email, create_user


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'db.sqlite3')
app.config.update(config_dict)

db.init_app(app)
jwt.init_app(app)


app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(roles, url_prefix='/roles')
# app.register_blueprint(products, url_prefix='/products')


if __name__ == "__main__":
    app.run(port=5001, debug=True, host='0.0.0.0')