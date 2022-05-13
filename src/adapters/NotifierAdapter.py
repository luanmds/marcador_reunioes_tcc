

from abc import ABC
from src.applicationCore.domain.reuniao.NotificadorReuniao import NotificadorReuniao


class NotifierAdapter(NotificadorReuniao, ABC):

    def __init__(self, mensagem: str):
        super().__init__(mensagem)
