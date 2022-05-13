from marshmallow import fields

from applicationCore.domain.reuniao.SalaEncontro import SalaEncontro


class SalaFisica(SalaEncontro):
    numero = fields.Int(allow_none=False)

    def getSalaInfoCompleta(self) -> str:
        return f'Sala: {self.nome} - {self.numero}'
