from abc import ABC , abstractmethod

class AtualizarLembreteInterface(ABC):
    """Interface para atualizar lembretes"""
    
    @abstractmethod
    def atualizar(self, id: int, dto: dict) -> dict:
        pass
