from marshmallow import fields

from applicationCore.domain.reuniao.SalaEncontro import SalaEncontro


class SalaVirtual(SalaEncontro):
    link = fields.Str(allow_none=False)

    def getSalaInfoCompleta(self) -> str:
        return f'Link da Sala {self.nome}: {self.link}'
