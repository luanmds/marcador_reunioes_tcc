
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
from src.adapters.DatabaseConnectionAdapter import DatabaseConnectionAdapter
from src.applicationCore.domain.reuniao.Reuniao import Reuniao


class IReuniaoRepository(ABC):

    _dbConnection: DatabaseConnectionAdapter

    def __init__(self, dbConnection: DatabaseConnectionAdapter) -> None:
        self._dbConnection = dbConnection

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
    def findById(self, reuniaoId: int) -> Optional[Reuniao]:
        raise NotImplementedError

    @abstractmethod
    def findAllBetweenDataInicioAndDataTerminoFromUsuario(self, dataInicio: datetime,
                                                          dataTermino: datetime, usuarioId: int) -> List[Reuniao]:
        raise NotImplementedError
