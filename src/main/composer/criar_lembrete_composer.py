from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.lembrete_repository import LembreteRepository
from src.services.criar_lembrete import CriarLembrete
from src.controllers.criar_lembrete_controller import CriarLembreteController

def criar_lembrete_composer () -> CriarLembreteController:
    model = LembreteRepository(postgres_connection_handler)
    service = CriarLembrete(model)
    controller = CriarLembreteController(service)
    return controller
