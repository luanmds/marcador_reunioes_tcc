
from dataclasses import dataclass


@dataclass
class DadosPessoais():
    """
    Classe representando o Objeto de Valor DadosPessoais complementar a Entidade Usuário

    Attributes:
        nome (str): nome completo do usuário.
        email (str): E-mail corporativo do usuário.
        telCelular (str): Número do telefone celular do usuário.
        cargo (str): Nome por extenso do Cargo pertecente ao usuário.
    """

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
