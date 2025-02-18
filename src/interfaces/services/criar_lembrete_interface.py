from abc import ABC, abstractmethod

class CriarLembreteInterface(ABC):
    """Interface para o serviço de criar lembrete"""
    
    @abstractmethod
    def criar(self, dto: dict) -> dict:
        pass
