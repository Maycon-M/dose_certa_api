from fastapi import HTTPException
from src.interfaces.models.lembrete_repository_interface import LembreteRepositoryInterface
from src.interfaces.services.listar_por_id_interface import ListarPorIdInterface

class ListarPorId(ListarPorIdInterface):
    """Classe para listar um lembrete por id."""
    
    def __init__(self, lembrete_repository: LembreteRepositoryInterface):
        self.__lembrete_repository = lembrete_repository

    def listar(self, id: int) -> dict:
        lembrete = self.__listar_do_db(id)
        
        return self.__formatar_resposta(lembrete)
        
    def __listar_do_db(self, id: int) -> dict:
        try:
            return self.__lembrete_repository.list_by_id(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def __formatar_resposta(self, lembrete: dict) -> dict:
        return {
            "data": {
                "type": "lembrete",
                "count": 1,
                "attributes": lembrete
            }
        }
