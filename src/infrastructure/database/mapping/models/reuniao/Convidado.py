
from marshmallow import Schema, fields

from applicationCore.domain.reuniao.Reuniao import Reuniao
from applicationCore.domain.usuario.Usuario import Usuario

class Convidado(Schema):
    aceitaReuniao = fields.Bool()
    usuario = fields.Nested(Usuario)

    def setAceitaReuniao(self, aceita: bool):
        self.aceitaReuniao = aceita
