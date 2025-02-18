from fastapi import HTTPException
from src.interfaces.models.lembrete_repository_interface import LembreteRepositoryInterface
from src.interfaces.services.listar_todos_interface import ListarTodosInterface

class ListarTodos(ListarTodosInterface):
    """Classe de serviço para listar todos os lembretes."""

    def __init__(self, lembrete_repository: LembreteRepositoryInterface):
        self.__lembrete_repository = lembrete_repository

    def listar(self) -> dict:
        return self.__formatar_resposta(self.__listar_do_db())

    def __listar_do_db(self) -> list:
        try:
            return self.__lembrete_repository.get_all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def __formatar_resposta(self, lembretes: list) -> dict:
        return {
            "data": {
                "type": "lembrete",
                "count": len(lembretes),
                "attributes": lembretes
            }
        }
