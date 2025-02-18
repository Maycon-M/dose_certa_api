from abc import ABC, abstractmethod
from sqlalchemy import Engine

class DBConnectionInterface(ABC):
    
    @abstractmethod
    def connect_to_db(self) -> Engine:
        pass
    
    @abstractmethod
    def get_engine(self) -> Engine:
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
