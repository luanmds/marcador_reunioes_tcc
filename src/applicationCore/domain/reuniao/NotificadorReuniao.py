
from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.applicationCore.domain.reuniao.Convidado import Convidado


@dataclass
class NotificadorReuniao(ABC):

    def __init__(self, mensagem: str):
        self._mensagem = mensagem

    @abstractmethod
    def enviarNotificacao(remetente: Convidado):
        raise NotImplementedError

    @property
    def mensagem(self) -> str:
        return self._mensagem

    @mensagem.setter
    def mensagem(self, nova_mensagem: str):
        self._mensagem = nova_mensagem
