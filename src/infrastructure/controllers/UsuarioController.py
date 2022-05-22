from datetime import datetime, timedelta
import json
from typing import Dict

import jwt
import os
from dependency_injector.wiring import Provide, inject
from flask import request
from flask_restx import Namespace, Resource, fields
from src.applicationCore.services.exceptions.UsuarioException import \
    UsuarioErrorCredentials
from src.applicationCore.services.usuario.UsuarioService import UsuarioService
from src.infrastructure.Dependencies import Dependencies

api = Namespace(
    'usuario', description='Operações envolvendo Usuário na aplicação')

user_auth = api.model('loginInfo', {
    'username': fields.String(required=True, description='Nome de login do usuário'),
    'senha': fields.String(required=True, description='Senha do usuário'),
})


@api.route('/login')
class UsuarioLogin(Resource):

    @api.doc('Login do Usuário')
    @api.expect(user_auth, validate=True)
    @inject
    def post(self, usuarioService: UsuarioService = Provide[Dependencies.usuarioService]) -> Dict:

        post_data = request.json

        try:
            usuario = usuarioService.fazerLogin(
                user=post_data['username'], senha=post_data['senha'])

            token = jwt.encode({
                'user_data': json.dumps(usuario),
                'exp': datetime.utcnow() + timedelta(days=1)
            }, os.getenv('SECRET_API_KEY'))

            return {
                "message": "Login de Usuário realizado com sucesso",
                "status": "success",
                "data": {
                    "auth_token": token
                }
            }

        except UsuarioErrorCredentials as e:
            return {
                "message": e.message,
                "status": "error"
            }, 401
