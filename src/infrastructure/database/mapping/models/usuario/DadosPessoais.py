
from marshmallow import Schema, fields


class DadosPessoais(Schema):
    nome = fields.Str(dump_only=True, allow_none=False)
    email = fields.Email(dump_only=True, allow_none=False)
    telCelular = fields.Str(dump_only=True, allow_none=False)
    cargo = fields.Str(dump_only=True, allow_none=False)
