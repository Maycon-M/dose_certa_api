from fastapi import HTTPException
from src.interfaces.models.lembrete_repository_interface import LembreteRepositoryInterface
from src.interfaces.services.deletar_lembrete_interface import DeletarLembreteInterface

class DeletarLembrete(DeletarLembreteInterface):
    """Classe para deletar um lembrete."""
    
    def __init__(self, lembrete_repository: LembreteRepositoryInterface):
        self.lembrete_repository = lembrete_repository

    def deletar (self, id: int) -> None:
        self.__deletar_no_db(id)    
    
    def __deletar_no_db (self, id: int) -> None:
        try:
            lembrete = self.lembrete_repository.get_by_id(id)
            if not lembrete:
                raise HTTPException(status_code=404, detail="Lembrete não encontrado.")
            self.lembrete_repository.delete(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
