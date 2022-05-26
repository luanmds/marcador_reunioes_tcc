
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SalaEncontro(ABC):

    def __init__(self, nome: str) -> None:
        super().__init__()
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        self._nome = novo_nome

    @abstractmethod
    def getSalaInfoCompleta(self) -> str:
        raise NotImplementedError
