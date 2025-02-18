from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.atualizar_lembrete_interface import AtualizarLembreteInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class AtualizarLembreteController (ControllerInterface):
    """Classe de controller para atualizar um lembrete."""
    
    def __init__(self, atualizar_lembrete_service: AtualizarLembreteInterface):
        self.__atualizar_lembrete_service = atualizar_lembrete_service
        
    def handle (self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.param.get('id')
        dto = http_request.body
        body_response = self.__atualizar_lembrete_service.atualizar(id, dto)
        return HttpResponse(status_code=200, body=body_response)
