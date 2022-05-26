from abc import ABC, abstractmethod


class DatabaseConnectionAdapter():
    _dbConnectionString: str

    def __init__(self, dbConnString: str) -> None:
        self._dbConnectionString = dbConnString

    def get_conn(self) -> object:
        raise NotImplementedError
