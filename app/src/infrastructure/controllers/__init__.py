from flask_restx import Api
from src.infrastructure.controllers.UsuarioController import api as ns_usuario


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


# init namespaces for API
api = Api(
    title="API Marcador de Reuniões",
    version="1.0",
    description="Api do Estudo de Caso voltado para marcar reuniões dentro da empresa Seguro Corp - Monografia",
    url_scheme="/api",
    authorizations=authorizations
)

api.add_namespace(ns_usuario)
