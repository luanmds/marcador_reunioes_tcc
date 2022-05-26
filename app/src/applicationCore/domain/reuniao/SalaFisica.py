from marshmallow import fields

from src.applicationCore.domain.reuniao.SalaEncontro import SalaEncontro


class SalaFisica(SalaEncontro):

    def __init__(self, nome: str, numero: int) -> None:
        super().__init__(nome)
        self._numero = numero

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, novo_numero: int):
        self._numero = novo_numero

    def getSalaInfoCompleta(self) -> str:
        return f'Sala {self._nome}: Número {self._numero}'
