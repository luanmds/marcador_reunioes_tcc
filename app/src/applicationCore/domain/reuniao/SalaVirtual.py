from marshmallow import fields

from src.applicationCore.domain.reuniao.SalaEncontro import SalaEncontro


class SalaVirtual(SalaEncontro):

    def __init__(self, nome: str, link: str) -> None:
        super().__init__(nome)
        self._link = link

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, novo_link: str):
        self._link = novo_link

    def getSalaInfoCompleta(self) -> str:
        return f'Sala {self._nome}:  {self._link}'
