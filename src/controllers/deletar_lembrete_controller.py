from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.deletar_lembrete_interface import DeletarLembreteInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class DeletarLembreteController (ControllerInterface):
    """Classe de controller para deletar um lembrete."""
    
    def __init__(self, deletar_lembrete_service: DeletarLembreteInterface):
        self.__deletar_lembrete_service = deletar_lembrete_service
        
    def handle (self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.param.get('id')
        return self.__deletar_lembrete_service.deletar(id)
