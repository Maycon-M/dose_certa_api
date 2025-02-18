from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.lembrete_repository import LembreteRepository
from src.services.deletar_lembrete import DeletarLembrete
from src.controllers.deletar_lembrete_controller import DeletarLembreteController

def deletar_lembrete_composer () -> DeletarLembreteController:
    model = LembreteRepository(postgres_connection_handler)
    service = DeletarLembrete(model)
    controller = DeletarLembreteController(service)
    return controller
