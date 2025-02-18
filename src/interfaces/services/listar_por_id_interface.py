from abc import ABC, abstractmethod

class ListarPorIdInterface(ABC):
    """Interface para listar por id"""
    
    @abstractmethod
    def listar(self, id: int) -> dict:
        pass
