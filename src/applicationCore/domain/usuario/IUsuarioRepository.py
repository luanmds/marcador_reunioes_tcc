
from abc import ABC, abstractmethod
from ast import Not

from src.applicationCore.domain.usuario.Usuario import Usuario


class IUsuarioRepository(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def findById(usuarioId: int) -> Usuario:
        raise NotImplementedError

    @abstractmethod
    def findByUsername(username: str) -> Usuario:
        raise NotImplementedError

    @abstractmethod
    def findByUsernameAndSenha(username: str, senha_encriptada: str) -> Usuario:
        raise NotImplementedError
