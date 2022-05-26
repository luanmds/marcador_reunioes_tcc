
from dataclasses import dataclass
from datetime import datetime

from typing import List


from src.applicationCore.domain.reuniao.Status import Status
from src.applicationCore.domain.reuniao.Lembrete import Lembrete

from src.applicationCore.domain.reuniao.SalaEncontro import SalaEncontro


@dataclass
class ReuniaoDTO():

    reuniaoId: int
    titulo: str
    pauta: str
    dataInicio: datetime
    dataFim: datetime
    local: SalaEncontro
    lembrete: Lembrete
    convidadosUsernames: List[str]
    status: Status

    def __init__(self, titulo: str, pauta: str, dataInicio: datetime, dataFim: datetime,
                 local: SalaEncontro, lembrete: Lembrete, convidadosUsernames: List[str],
                 reuniaoId: int = 0, status: Status = Status.MARCADA) -> None:

        self.reuniaoId = reuniaoId
        self.titulo = titulo
        self.pauta = pauta
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.local = local
        self.lembrete = lembrete
        self.convidadosUsernames = convidadosUsernames
        self.status = status
