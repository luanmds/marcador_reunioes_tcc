
from abc import ABC, abstractmethod
from ast import Not
from datetime import date, datetime
from src.applicationCore.domain.reuniao.Reuniao import Reuniao
from src.applicationCore.domain.usuario.Usuario import Usuario


class IReuniaoRepository(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def save(reuniao: Reuniao) -> int:
        raise NotImplementedError

    @abstractmethod
    def update(reuniao: Reuniao) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(reuniao: Reuniao) -> bool:
        raise NotImplementedError

    @abstractmethod
    def findAllBetweenDataInicioAndDataTerminoFromUsuario(dataInicio: datetime,
                                                          dataTermino: datetime, usuario: Usuario) -> Reuniao:
        raise NotImplementedError

    @abstractmethod
    def findByUsername(username: str) -> Reuniao:
        raise NotImplementedError

    @abstractmethod
    def findByUsernameAndSenha(username: str, senha_encriptada: str) -> Reuniao:
        raise NotImplementedError
