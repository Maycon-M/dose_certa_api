from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.lembrete_repository import LembreteRepository
from src.services.listar_por_id import ListarPorId
from src.controllers.listar_por_id_controller import ListarPorIdController

def listar_por_id_composer () -> ListarPorIdController:
    model = LembreteRepository(postgres_connection_handler)
    service = ListarPorId(model)
    controller = ListarPorIdController(service)
    return controller
