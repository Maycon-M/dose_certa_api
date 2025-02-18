from abc import ABC, abstractmethod

class LembreteRepositoryInterface(ABC):
    """Interface para o repositório de lembretes."""
    
    @abstractmethod
    def create(self, dto: dict) -> None:
        pass
    
    @abstractmethod
    def get_all(self) -> list:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> list:
        pass
    
    @abstractmethod
    def update(self, dto: dict) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
