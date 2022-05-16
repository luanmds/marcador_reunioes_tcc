
from abc import ABC, abstractmethod
from ast import Not
from typing import List, Optional

from src.applicationCore.domain.usuario.Usuario import Usuario


class IUsuarioRepository(ABC):

    def __init__(self) -> None:
        super().__init__()

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
