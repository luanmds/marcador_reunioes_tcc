
from abc import ABC, abstractmethod
from ast import Not
from typing import List

from src.applicationCore.domain.usuario.Usuario import Usuario


class IUsuarioRepository(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def findById(self, usuarioId: int) -> Usuario:
        raise NotImplementedError

    @abstractmethod
    def findByNomeOrUsername(self, palavras: List[str]) -> List[Usuario]:
        raise NotImplementedError

    @abstractmethod
    def findByUsername(self, username: str) -> Usuario:
        raise NotImplementedError

    @abstractmethod
    def findByUsernameAndSenha(self, username: str, senha_encriptada: str) -> Usuario:
        raise NotImplementedError
