import dataclasses
import os
from datetime import datetime, timedelta

import jwt
from dependency_injector.wiring import Provide, inject
from flask import request
from flask_restx import Namespace, Resource, fields
from src.applicationCore.services.usuario.UsuarioBasico import UsuarioBasico
from src.applicationCore.services.exceptions.UsuarioException import \
    UsuarioErrorCredentials
from src.applicationCore.services.usuario.UsuarioService import UsuarioService
from src.infrastructure.Dependencies import Dependencies
from src.utils.token_required import token_required

api = Namespace(
    'usuario', description='Operações envolvendo Usuário na aplicação')

user_auth = api.model('loginInfo', {
    'username': fields.String(required=True, description='Nome de login do usuário'),
    'senha': fields.String(required=True, description='Senha do usuário'),
})

usernames_list = api.model('listUsernames', {
    'usernames': fields.List(fields.String(), required=True, description="lista de usernames")
})


@api.route('/login')
class UsuarioLogin(Resource):

    @api.doc('Login do Usuário')
    @api.expect(user_auth, validate=True)
    @inject
    def post(self, usuarioService: UsuarioService = Provide[Dependencies.usuarioService]):

        post_data = request.json

        try:
            usuario = usuarioService.fazerLogin(
                user=post_data['username'], senha=post_data['senha'])

            token = jwt.encode({
                'user_data': dataclasses.asdict(usuario),
                'exp': datetime.utcnow() + timedelta(days=1)
            }, os.getenv('SECRET_API_KEY'))

            return {
                "message": "Login de Usuário realizado com sucesso",
                "status": "success",
                "data": {
                    "auth_token": token
                }
            }, 200

        except UsuarioErrorCredentials as e:
            return {
                "message": e.message,
                "status": "error"
            }, 401


@api.route('/buscar')
class UsuarioFind(Resource):

    @api.doc('Busca Usuários através de uma lista de Usernames', security='apikey')
    @api.param('usernames', 'Lista de Usernames separados por espaço em branco', validate=True)
    @token_required
    @inject
    def get(self, current_user: UsuarioBasico, usuarioService: UsuarioService = Provide[Dependencies.usuarioService]):

        data = request.args.to_dict()

        if not data['usernames']:
            return api.abort(400)

        usuarios = usuarioService.buscaUsuariosPorNomeOuUsername(
            data['usernames'].split(" "))

        return {
            "message": "Login de Usuário realizado com sucesso",
            "status": "success",
            "data": {
                "usuariosEncontrados": [dataclasses.asdict(u) for u in usuarios]
            }}, 200
