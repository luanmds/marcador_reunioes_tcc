
from src.applicationCore.services.exceptions.ApplicationException import ApplicationException


class UsuarioException(ApplicationException):
    pass


class UsuarioErrorCredentials(UsuarioException):

    def __init__(self, username: str) -> None:
        self.username = username
        self.message = f"Usuário ou Senha inválidos."
        super().__init__(self.message)
