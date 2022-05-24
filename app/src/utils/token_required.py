# token decorator for validation JWT

import os
from functools import wraps

import jwt
from flask import request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {"message": "Token is missing."}, 401

        try:
            data = jwt.decode(token, os.getenv(
                'SECRET_API_KEY'), algorithms=["HS256"])
            current_user = data['user_data']
            print(current_user)
        except:
            return {"message": "Token is invalid."}, 401

        return f(current_user, *args, **kwargs)

    return decorated
