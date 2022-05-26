
from src.adapters.DatabaseConnectionAdapter import DatabaseConnectionAdapter
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class DbSqlConnection(DatabaseConnectionAdapter):

    _engine = None

    def __init__(self, user: str, password: str, host: str, database: str) -> None:
        dbConnString = f"mysql+mysqlconnector://{user}:{password}@{host}:3306/{database}"
        super().__init__(dbConnString)
        self._engine = create_engine(dbConnString)

    def get_conn(self) -> Session:
        return Session(bind=self._engine)
