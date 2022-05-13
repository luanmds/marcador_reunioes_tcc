
from abc import ABC, abstractmethod
from marshmallow import Schema, fields, validate
from applicationCore.domain.reuniao.Convidado import Convidado


class NotificadorReuniao(ABC, Schema):

    mensagem = fields.Str(required=True,
                          allow_none=False, validate=validate.Length(min=5, max=255))

    @abstractmethod
    def enviarNotificacao(remetente: Convidado):
        raise NotImplementedError

    @abstractmethod
    def setMensagem(nova_msg: str):
        raise NotImplementedError
