from models import User


def get_user_by_email(email:str) -> (User, None):
    return User.query.filter_by(email=email).one_or_none()


def get_user_by_id(user_id: int) -> (User, None):
    return User.query.filter_by(id=user_id).one_or_none()


def create_user(**kwargs):
    user = User(
        email=kwargs['email'],
        password=User.hash_password(kwargs['password'])
    )
    return user