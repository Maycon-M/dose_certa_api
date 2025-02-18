from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.lembrete_repository import LembreteRepository
from src.services.atualizar_lembrete import AtualizarLembrete
from src.controllers.atualizar_lembrete_controller import AtualizarLembreteController

def atualizar_lembrete_composer () -> AtualizarLembreteController:
    model = LembreteRepository(postgres_connection_handler)
    service = AtualizarLembrete(model)
    controller = AtualizarLembreteController(service)
    return controller
