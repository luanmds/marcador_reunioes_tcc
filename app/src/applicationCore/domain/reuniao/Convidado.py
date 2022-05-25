
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

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    def __eq__(self, other):
        return self._usuario.id == other.usuario.id
