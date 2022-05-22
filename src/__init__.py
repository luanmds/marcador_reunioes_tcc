import os
from flask import Flask
from flask_restx import Api

import src
from src.infrastructure.controllers.UsuarioController import api as ns_usuario
from src.infrastructure.Dependencies import Dependencies
import jwt
from flask import jsonify, request
from functools import wraps


app = Flask(__name__)

# app configurations
app.config.from_pyfile('../config.py')

# init Dependencies to Injection
dependencies = Dependencies()
dependencies.init_resources()
dependencies.wire(packages=[src])

app.container = dependencies

# token decorator for validation JWT


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing.'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_API_KEY'])
            current_user = data.user_data
            print(current_user)
        except:
            return jsonify({'message': 'Token is invalid.'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# init namespaces for API


api = Api(
    title="API Marcador de Reuniões",
    version="1.0",
    description="Api do Estudo de Caso voltado para marcar reuniões dentro da empresa Seguro Corp - Monografia",
    url_scheme="/api"
)

api.add_namespace(ns_usuario)
api.init_app(app)
