
from dataclasses import dataclass
from datetime import datetime
from tkinter import LEFT
from typing import List
from applicationCore.domain.reuniao.NotificadorReuniao import NotificadorReuniao
from applicationCore.domain.reuniao.SalaEncontro import SalaEncontro

from applicationCore.domain.reuniao.Convidado import Convidado
from applicationCore.domain.reuniao.Status import Status
from applicationCore.domain.reuniao.Lembrete import Lembrete

from applicationCore.domain.usuario.Usuario import Usuario
from src.applicationCore.domain.Entity import Entity


@dataclass
class Reuniao(Entity):

    def __init__(self, reuniaoId: int, titulo: str, pauta: str, dataInicio: datetime,
                 dataTermino: datetime, host: Usuario, sala: SalaEncontro, status: Status = Status.MARCADA,
                 lembrete: Lembrete = Lembrete.QUINZE_MINUTOS, convidados: List[Convidado] = None):
        super().__init__(reuniaoId)
        self._titulo = titulo
        self._pauta = pauta
        self._dataInicio = dataInicio
        self._dataTermino = dataTermino
        self._status = status
        self._lembrete = lembrete
        self._host = host
        self._sala = sala
        self._convidados = convidados
        self._notificadorReuniao: NotificadorReuniao = None

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo: str):
        self._titulo = novo_titulo

    @property
    def pauta(self) -> str:
        return self._pauta

    @pauta.setter
    def pauta(self, nova_pauta: str):
        self._pauta = nova_pauta

    @property
    def dataInicio(self) -> datetime:
        return self._dataInicio

    @dataInicio.setter
    def dataInicio(self, novo_dataInicio: datetime):
        self._dataInicio = novo_dataInicio

    @property
    def dataTermino(self) -> datetime:
        return self._dataTermino

    @dataTermino.setter
    def dataTermino(self, novo_dataTermino: datetime):
        self._dataTermino = novo_dataTermino

    @property
    def status(self) -> Status:
        return self._status

    @property
    def lembrete(self) -> Lembrete:
        return self._lembrete

    @lembrete.setter
    def lembrete(self, novo_lembrete: Lembrete):
        self._lembrete = novo_lembrete

    @property
    def convidados(self) -> List[Convidado]:
        return self._convidados

    def addConvidado(self, convidado: Convidado):
        self._convidados.append(convidado)

    def concluirReuniao(self) -> bool:
        self._status = Status.CONCLUIDA
        return True

    def cancelarReuniao(self) -> bool:
        self._status = Status.CANCELADA
