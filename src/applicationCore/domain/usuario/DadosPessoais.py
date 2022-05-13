
from dataclasses import dataclass


@dataclass
class DadosPessoais():

    def __init__(self, nome: str, email: str, telCelular: str, cargo: str) -> None:
        self._nome = nome
        self._email = email
        self._telCelular = telCelular
        self._cargo = cargo

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
