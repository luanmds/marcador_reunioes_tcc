
from abc import ABC, abstractmethod


class SalaEncontro(ABC):

    def __init__(self, salaEncontroId: int, nome: str) -> None:
        super().__init__()
        self._salaEncontroId = salaEncontroId
        self._nome = nome

    @property
    def salaEncontroId(self) -> int:
        return self._salaEncontroId

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        self._nome = novo_nome

    @abstractmethod
    def getSalaInfoCompleta() -> str:
        raise NotImplementedError
