from src.interfaces.models.db_connection_interface import DBConnectionInterface
from src.interfaces.models.lembrete_repository_interface import LembreteRepositoryInterface
from src.models.entities.lembrete import LembreteTable


class LembreteRepository(LembreteRepositoryInterface):
    """Classe que representa o repositório de lembretes."""
    
    def __init__(self, db_connection: DBConnectionInterface):
        self.__db_connection = db_connection

    def create(self, dto: dict) -> None:
        with self.__db_connection as database:
            try:
                data_obj = LembreteTable(
                    nome=dto.get("nome"),
                    quantidade=dto.get("quantidade"),
                    horario=dto.get("horario")
                )
                database.session.add(data_obj)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
            
    def get_all(self) -> list[LembreteTable]:
        with self.__db_connection as database:
            try:
                return database.session.query(LembreteTable).all()
            except Exception as e:
                raise e
            
    def get_by_id(self, id: int) -> LembreteTable:
        with self.__db_connection as database:
            try:
                return database.session.query(LembreteTable).filter(LembreteTable.id == id).first()
            except Exception as e:
                raise e

    def update(self, dto: dict, id: int) -> None:
        with self.__db_connection as database:
            try:
                nome=dto.get("nome")
                quantidade=dto.get("quantidade")
                horario=dto.get("horario")

                database.session.query(LembreteTable).filter(LembreteTable.id == id).update({LembreteTable.nome: nome, LembreteTable.quantidade: quantidade, LembreteTable.horario: horario})
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e

    def delete(self, id: int) -> None:
        with self.__db_connection as database:
            try:
                database.session.query(LembreteTable).filter(LembreteTable.id == id).delete()
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
