
class DatabaseConnectionAdapter():
    _dbConnectionString: str

    def __init__(self, dbConnString: str) -> None:
        self._dbConnectionString = dbConnString
