
from marshmallow import Schema, fields

from applicationCore.domain.usuario.DadosPessoais import DadosPessoais


class Usuario(Schema):
    usuarioId = fields.Integer()
    username = fields.Str(required=True, allow_none=False)
    senha = fields.Str(load_only=True, allow_none=True)
    dadosPessoais = fields.Nested(DadosPessoais)
