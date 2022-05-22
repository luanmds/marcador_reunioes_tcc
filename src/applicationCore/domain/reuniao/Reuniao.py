
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from src.applicationCore.domain.reuniao.NotificadorReuniao import NotificadorReuniao
from src.applicationCore.domain.reuniao.SalaEncontro import SalaEncontro

from src.applicationCore.domain.reuniao.Convidado import Convidado
from src.applicationCore.domain.reuniao.Status import Status
from src.applicationCore.domain.reuniao.Lembrete import Lembrete

from src.applicationCore.domain.usuario.Usuario import Usuario
from src.applicationCore.domain.Entity import Entity


@dataclass
class Reuniao(Entity):
    """
    Classe representando a entidade Reuniao

    Attributes:
        id (int): identificador único da entidade (herdado da classe Entity).
        titulo (str): título apresentado na reunião.
        pauta (str): pauta da reunião para entendimento dos participantes.
        dataInicio (datetime): data e hora de inicio da reunião.
        dataTermino (datetime): data e hora do fim da reunião.
        host (Usuario): criador e anfitrião da reunião.
        sala (SalaEncontro): local VusuarioIdrtual ou Fisico, que irá ocorrer a reunião.
        status (Status): representa o estado atual da reunião.
        lembrete (Lembrete): minutagem a ser acionada para lembrar do ínicio da reunião.
        convidados (List[Convidado]): lista de convidados participantes da reunião.
        notificadores (List[NotificadorReuniao]): lista de tipos de notificações de mudanças na reunião para cada convidado.
    """

    def __init__(self, reuniaoId: int, titulo: str, pauta: str, dataInicio: datetime,
                 dataTermino: datetime, host: Usuario, sala: SalaEncontro, status: Status = Status.MARCADA,
                 lembrete: Lembrete = Lembrete.QUINZE_MINUTOS,
                 convidados: List[Convidado] = field(default_factory=list),
                 notificadores: List[NotificadorReuniao] = field(default_factory=list)):
        super().__init__(reuniaoId)
        self._titulo = titulo
        self._pauta = pauta
        self._dataInicio = dataInicio
        self._dataTermino = dataTermino
        self._status = status
        self._lembrete = lembrete
        self._host = host
        self._sala = sala
        self._convidados: List[Convidado] = convidados
        self._notificadorReuniao: List[NotificadorReuniao] = notificadores

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

    @property
    def host(self) -> Usuario:
        return self._host

    @property
    def sala(self) -> SalaEncontro:
        return self._sala

    @sala.setter
    def sala(self, nova_sala: SalaEncontro):
        self._sala = nova_sala

    @property
    def notificadores(self) -> List[NotificadorReuniao]:
        return self._notificadorReuniao

    @notificadores.setter
    def notificadores(self, notificadores: List[NotificadorReuniao]):
        self._notificadorReuniao = notificadores

    def adicionarConvidado(self, convidado: Convidado) -> None:
        self._convidados.append(convidado)

    def removerConvidado(self, convidado: Convidado) -> None:
        self._convidados.pop(convidado)

    def concluirReuniao(self) -> bool:
        self._status = Status.CONCLUIDA
        return True

    def cancelarReuniao(self) -> bool:
        self._status = Status.CANCELADA
        return True

    def enviarNotificacoes(self) -> bool:
        for n in self._notificadorReuniao:
            for c in self._convidados:
                n.enviarNotificacao(remetente=c)
