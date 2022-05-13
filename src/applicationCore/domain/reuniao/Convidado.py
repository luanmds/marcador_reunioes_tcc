
from dataclasses import dataclass
from src.applicationCore.domain.usuario.Usuario import Usuario


@dataclass
class Convidado():

    def __init__(self, aceitaReuniao: bool, usuario: Usuario) -> None:
        self._aceitaReuniao = aceitaReuniao
        self._usuario = usuario

    @property
    def aceitaReuniao(self) -> bool:
        return self._aceitaReuniao

    @aceitaReuniao.setter
    def aceitaReuniao(self, aceita: bool):
        self._aceitaReuniao = aceita
