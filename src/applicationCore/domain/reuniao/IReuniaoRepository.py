
from abc import ABC, abstractmethod
from ast import Not
from datetime import date, datetime
from typing import List
from src.applicationCore.domain.reuniao.Reuniao import Reuniao


class IReuniaoRepository(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def save(self, reuniao: Reuniao) -> int:
        raise NotImplementedError

    @abstractmethod
    def update(self, reuniao: Reuniao) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, reuniao: Reuniao) -> bool:
        raise NotImplementedError

    @abstractmethod
    def findById(self, reuniaoId: int) -> Reuniao:
        raise NotImplementedError

    @abstractmethod
    def findAllBetweenDataInicioAndDataTerminoFromUsuario(self, dataInicio: datetime,
                                                          dataTermino: datetime, usuarioId: int) -> List[Reuniao]:
        raise NotImplementedError
