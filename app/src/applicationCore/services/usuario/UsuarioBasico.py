
from dataclasses import dataclass


@dataclass
class UsuarioBasico():
    """
    Classe de Dados Simplificado da Entidade Usuário

    Attributes:
        username (str): nome de usuário único.            
        nome (str): nome completo do usuário.
        email (str): E-mail corporativo do usuário.
        telCelular (str): Número do telefone celular do usuário.
        cargo (str): Nome por extenso do Cargo pertecente ao usuário.
    """

    username: str
    nome: str
    email: str
    telCelular: str
    cargo: str

    def __init__(self, username: str, nome: str, email: str,
                 telCelular: str, cargo: str) -> None:
        self.username = username
        self.nome = nome
        self.email = email
        self.telCelular = telCelular
        self.cargo = cargo
