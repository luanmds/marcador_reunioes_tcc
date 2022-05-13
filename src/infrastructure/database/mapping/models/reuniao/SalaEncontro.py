
from abc import ABC, abstractmethod
from marshmallow import Schema, fields, validate


class SalaEncontro(ABC, Schema):
    salaEncontroId = fields.Int()
    nome = fields.Str(allow_none=False, validate=validate.Length(min=3))

    @abstractmethod
    def getSalaInfoCompleta() -> str:
        raise NotImplementedError
