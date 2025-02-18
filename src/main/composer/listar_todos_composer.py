from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.lembrete_repository import LembreteRepository
from src.services.listar_todos import ListarTodos
from src.controllers.listar_todos_controller import ListarTodosController

def listar_todos_composer () -> ListarTodosController:
    model = LembreteRepository(postgres_connection_handler)
    service = ListarTodos(model)
    controller = ListarTodosController(service)
    return controller
