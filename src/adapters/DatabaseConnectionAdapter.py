from abc import ABC, abstractmethod


class DatabaseConnectionAdapter(ABC):
    _dbConnectionString: str

    def __init__(self, dbConnString: str) -> None:
        self._dbConnectionString = dbConnString

    @abstractmethod
    def get_conn(self) -> object:
        raise NotImplementedError
