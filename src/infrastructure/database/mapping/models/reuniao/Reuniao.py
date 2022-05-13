from marshmallow import Schema, fields
from applicationCore.domain.reuniao.NotificadorReuniao import NotificadorReuniao
from applicationCore.domain.reuniao.SalaEncontro import SalaEncontro
from marshmallow_enum import EnumField

from applicationCore.domain.reuniao.Convidado import Convidado
from applicationCore.domain.reuniao.Status import Status
from applicationCore.domain.reuniao.Lembrete import Lembrete

from applicationCore.domain.usuario.Usuario import Usuario


class Reuniao(Schema):
    reuniaoId = fields.Integer()
    titulo = fields.String(allow_none=False)
    pauta = fields.String(allow_none=False)
    dataInicio = fields.DateTime(allow_none=False)
    dataTermino = fields.DateTime(allow_none=False)
    status = EnumField(Status)
    lembrete = EnumField(Lembrete)
    host = fields.Nested(Usuario)
    convidados = fields.List(fields.Nested(Convidado))
    sala = fields.Nested(SalaEncontro)
    notificadorReuniao = fields.List(
        fields.Nested(NotificadorReuniao), allow_none=True)

    set
