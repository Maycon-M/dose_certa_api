from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.criar_lembrete_interface import CriarLembreteInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class CriarLembreteController (ControllerInterface):
    """Classe de controller para criar um lembrete."""
    
    def __init__(self, criar_lembrete_service: CriarLembreteInterface):
        self.__criar_lembrete_service = criar_lembrete_service
        
    def handle (self, http_request: HttpRequest) -> HttpResponse:
        dto = http_request.body
        body_response = self.__criar_lembrete_service.criar(dto)
        return HttpResponse(status_code=201, body=body_response)
