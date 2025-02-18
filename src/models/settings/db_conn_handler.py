from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from src.configs.database import DATABASE_URL
from src.interfaces.models.db_connection_interface import DBConnectionInterface

class PostgresConnectionHandler(DBConnectionInterface):
    """
    Essa classe é responsável por criar a conexÃ£o com o banco de dados PostgreSQL.
    """

    def __init__(self) -> None:
        self.__connection_string = DATABASE_URL
        self.__engine = None
        self.session = None

    def connect_to_db(self) -> Engine:
        """Cria a engine para conexÃ£o com o banco de dados."""
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        """Retorna a engine do banco de dados, criando-a se necessÃ¡rio."""
        if self.__engine is None:
            self.connect_to_db()
        return self.__engine

    def __enter__(self):
        """Inicia uma sessÃ£o para ser usada dentro de um contexto (with statement)."""
        session_maker = sessionmaker(autocommit=False, autoflush=False)
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Fecha a sessÃ£o ao sair do contexto."""
        self.session.close()

"""
    Essa variÃ¡vel Ã© responsÃ¡vel por instanciar a classe PostgresConnectionHandler. (Singleton)
"""
postgres_connection_handler = PostgresConnectionHandler()
