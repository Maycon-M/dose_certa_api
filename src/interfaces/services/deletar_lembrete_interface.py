from abc import ABC, abstractmethod

class DeletarLembreteInterface(ABC):
    """Interface para o método deletar de DeletarLembrete."""
    
    @abstractmethod
    def deletar (self, id: int) -> None:
        pass
