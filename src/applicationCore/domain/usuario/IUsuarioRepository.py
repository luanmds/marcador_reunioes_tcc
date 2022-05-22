
from abc import ABC, abstractmethod
from typing import List, Optional
from src.adapters.DatabaseConnectionAdapter import DatabaseConnectionAdapter

from src.applicationCore.domain.usuario.Usuario import Usuario


class IUsuarioRepository(ABC):

    _dbConnection: DatabaseConnectionAdapter

    def __init__(self, dbConnection: DatabaseConnectionAdapter) -> None:
        self._dbConnection = dbConnection

    @abstractmethod
    def findById(self, usuarioId: int) -> Optional[Usuario]:
        raise NotImplementedError

    @abstractmethod
    def findByNomeOrUsername(self, palavras: List[str]) -> List[Usuario]:
        raise NotImplementedError

    @abstractmethod
    def findByUsername(self, username: str) -> Optional[Usuario]:
        raise NotImplementedError

    @abstractmethod
    def findByUsernameAndSenha(self, username: str, senha_encriptada: str) -> Optional[Usuario]:
        raise NotImplementedError
