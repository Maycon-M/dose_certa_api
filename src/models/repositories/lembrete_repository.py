from src.interfaces.models.db_connection_interface import DBConnectionInterface
from src.interfaces.models.lembrete_repository_interface import LembreteRepositoryInterface
from src.models.entities.lembrete import LembreteTable


class LembreteRepository(LembreteRepositoryInterface):
    """Classe que representa o repositório de lembretes."""
    
    def __init__(self, db_connection: DBConnectionInterface):
        self.__db_connection = db_connection

    def create(self, dto: dict) -> None:
        with self.__db_connection.get_session() as session:
            try:
                data_obj = LembreteTable(
                    nome=dto.get("nome"),
                    quantidade=dto.get("quantidade"),
                    horario=dto.get("horario")
                )
                session.add(data_obj)
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
            
    def get_all(self) -> list:
        with self.__db_connection.get_session() as session:
            try:
                return session.query(LembreteTable).all()
            except Exception as e:
                raise e
            
    def get_by_id(self, id: int) -> list:
        with self.__db_connection.get_session() as session:
            try:
                return session.query(LembreteTable).filter(LembreteTable.id == id).first()
            except Exception as e:
                raise e

    def update(self, dto: dict) -> None:
        with self.__db_connection.get_session() as session:
            try:
                lembrete = LembreteTable(
                    nome=dto.get("nome"),
                    quantidade=dto.get("quantidade"),
                    horario=dto.get("horario")
                )
                session.query(LembreteTable).filter(LembreteTable.id == dto.get("id")).update(lembrete)
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def delete(self, id: int) -> None:
        with self.__db_connection.get_session() as session:
            try:
                session.query(LembreteTable).filter(LembreteTable.id == id).delete()
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
