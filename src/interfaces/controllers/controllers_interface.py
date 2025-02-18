from abc import ABC, abstractmethod
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class ControllerInterface (ABC):
    """Classe interface para todas as classe do tipo controller."""    
    
    @abstractmethod
    def handle (self, http_request: HttpRequest) -> HttpResponse:
        pass
