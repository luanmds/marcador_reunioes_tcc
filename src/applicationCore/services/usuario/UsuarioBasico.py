
from dataclasses import dataclass


@dataclass
class UsuarioBasico():

    def __init__(self, username: str, nome: str, email: str,
                 telCelular: str, cargo: str) -> None:
        self._username = username
        self._nome = nome
        self._email = email
        self._telCelular = telCelular
        self._cargo = cargo

    @property
    def username(self) -> str:
        return self._username

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def email(self) -> str:
        return self._email

    @property
    def telCelular(self) -> str:
        return self._telCelular

    @property
    def cargo(self) -> str:
        return self._cargo
