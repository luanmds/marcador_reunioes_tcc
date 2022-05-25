
from src.applicationCore.services.exceptions.ApplicationException import ApplicationException


class ReuniaoException(ApplicationException):
    pass


class ReuniaoNotFound(ReuniaoException):

    def __init__(self, reuniaoId: int) -> None:

        self.reuniaoId = reuniaoId
        self.message = f"Reunião {reuniaoId}, não foi encontrada."
        super().__init__(self.message)


class ConvidadoNotFound(ReuniaoException):

    def __init__(self, username: str) -> None:

        self.username = username
        self.message = f"Convidado {username}, não foi encontrado."
        super().__init__(self.message)


class ReuniaoCancelada(ReuniaoException):

    def __init__(self, reuniaoId: int) -> None:

        self.reuniaoId = reuniaoId
        self.message = f"Reunião {reuniaoId} foi cancelada e não pode ser atualizada."
        super().__init__(self.message)
