
from src.applicationCore.services.exceptions.ApplicationException import ApplicationException


class ReuniaoException(ApplicationException):
    pass


class ReuniaoNotFound(ReuniaoException):

    def __init__(self, reuniaoId: int) -> None:

        self.reuniaoId = reuniaoId
        self.message = f"Reunião {reuniaoId}, não foi encontrada."
        super().__init__(self.message)
