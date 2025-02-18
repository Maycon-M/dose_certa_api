from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.listar_todos_interface import ListarTodosInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class ListarTodosController(ControllerInterface):
    """Classe de controller para listar todos os lembretes."""

    def __init__(self, listar_todos_service: ListarTodosInterface):
        self.__listar_todos_service = listar_todos_service

    def handle(self, request: HttpRequest) -> HttpResponse:
        body_response = self.__listar_todos_service.listar()
        return HttpResponse(status_code=200, body=body_response)
