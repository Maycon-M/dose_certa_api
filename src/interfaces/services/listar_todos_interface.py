from abc import ABC, abstractmethod

class ListarTodosInterface(ABC):
    """Interface para listar todos os registros de uma entidade."""
    
    @abstractmethod
    def listar(self):
        pass
