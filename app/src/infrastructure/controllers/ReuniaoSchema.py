
from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from src.applicationCore.domain.reuniao.Status import Status

from src.applicationCore.domain.reuniao.Lembrete import Lembrete


class SalaEncontroSchema(Schema):
    nome = fields.Str()
    numero = fields.Integer()
    link = fields.Str()


class ReuniaoSchema(Schema):
    reuniaoId = fields.Integer()
    titulo = fields.Str()
    pauta = fields.Str()
    dataInicio = fields.DateTime('%Y-%m-%d %H:%M')
    dataFim = fields.DateTime('%Y-%m-%d %H:%M')
    local = fields.Nested(SalaEncontroSchema)
    lembrete = EnumField(Lembrete, by_value=True)
    status = EnumField(Status, by_value=True)
    convidadosUsernames = fields.List(fields.Str())
