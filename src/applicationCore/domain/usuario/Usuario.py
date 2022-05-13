from dataclasses import dataclass

from src.applicationCore.domain.Entity import Entity
from src.applicationCore.domain.usuario.DadosPessoais import DadosPessoais


@dataclass
class Usuario(Entity):

    def __init__(self, usuario_id: int, username: str, senha: str,
                 dadosPessoais: DadosPessoais) -> None:
        super().__init__(usuario_id)
        self._username = username
        self._senha = senha
        self._dadosPessoais = dadosPessoais

    @property
    def username(self) -> str:
        return self._username

    @property
    def senha(self) -> str:
        return self._senha

    @property
    def dadosPessoais(self) -> str:
        return self._dadosPessoais
