import json

from flask import Response
from flask_jwt_extended import current_user


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