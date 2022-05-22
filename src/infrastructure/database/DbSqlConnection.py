
from src.adapters.DatabaseConnectionAdapter import DatabaseConnectionAdapter
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session


class DbSqlConnection(DatabaseConnectionAdapter):

    _engine = None

    def __init__(self, dbConnString: str) -> None:
        super().__init__(dbConnString)
        self._engine = create_engine(dbConnString)

    def get_conn(self) -> Connection:
        return Session(bind=self._engine)
