from abc import ABC, abstractmethod
from src.models.entities.lembrete import LembreteTable

class LembreteRepositoryInterface(ABC):
    """Interface para o repositório de lembretes."""
    
    @abstractmethod
    def create(self, dto: dict) -> None:
        pass
    
    @abstractmethod
    def get_all(self) -> list[LembreteTable]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> LembreteTable:
        pass
    
    @abstractmethod
    def update(self, dto: dict) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
