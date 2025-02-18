from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.listar_por_id_interface import ListarPorIdInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class ListarPorIdController(ControllerInterface):
    """Classe de controller para listar um lembrete por ID."""

    def __init__(self, listar_por_id_service: ListarPorIdInterface):
        self.__listar_por_id_service = listar_por_id_service

    def handle(self, request: HttpRequest) -> HttpResponse:
        lembrete_id = request.param.get("id")
        body_response = self.__listar_por_id_service.listar(lembrete_id)
        return HttpResponse(status_code=200, body=body_response)
