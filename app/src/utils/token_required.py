# token decorator for validation JWT

import os
from functools import wraps

import jwt
from flask import request

from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico


def token_required(f):
    @wraps(f)
    def decorated(self, *args, **kwargs):
        token = None
        current_user = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {"message": "Token is missing."}, 401

        try:
            data = jwt.decode(token, os.getenv(
                'SECRET_API_KEY'), algorithms=["HS256"])

            current_user = UsuarioBasico(
                username=data['user_data']['username'],
                nome=data['user_data']['nome'],
                email=data['user_data']['email'],
                telCelular=data['user_data']['telCelular'],
                cargo=data['user_data']['cargo']
            )

            print("Usuário Logado: " + current_user.username)

        except Exception as e:
            return {"message": "Token is invalid."}, 401

        return f(self, current_user, *args, **kwargs)

    return decorated
