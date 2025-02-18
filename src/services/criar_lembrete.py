from fastapi import HTTPException
from src.interfaces.models.lembrete_repository_interface import LembreteRepositoryInterface
from src.interfaces.services.criar_lembrete_interface import CriarLembreteInterface

class CriarLembrete(CriarLembreteInterface):
    """Classe de serviço para criar um lembrete."""

    def __init__(self, lembrete_repository: LembreteRepositoryInterface):
        self.__lembrete_repository = lembrete_repository

    def criar(self, dto: dict) -> dict:
        self.__validar_dados(dto)

        dto["nome"] = dto["nome"].strip()
        dto["quantidade"] = int(dto["quantidade"])

        self.__criar_no_db(dto)

        return self.__formatar_resposta(dto)

    def __validar_dados(self, dto: dict) -> None:
        if not isinstance(dto, dict):
            raise HTTPException(status_code=422, detail="O dto precisa ser um dicionário")

        required_fields = ["nome", "quantidade", "horario"]
        for field in required_fields:
            if field not in dto or not dto[field]:
                raise HTTPException(status_code=422, detail=f"O campo '{field}' é obrigatório e não pode estar vazio.")

        if not isinstance(dto.get("nome"), str):
            raise HTTPException(status_code=422, detail="O nome precisa ser uma string")

        if not isinstance(dto.get("quantidade"), int):
            raise HTTPException(status_code=422, detail="A quantidade precisa ser um inteiro")

        if not isinstance(dto.get("horario"), str):
            raise HTTPException(status_code=422, detail="O horário precisa ser uma string")

    def __criar_no_db(self, dto: dict) -> None:
        try:
            self.__lembrete_repository.create(dto)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def __formatar_resposta (self, dto: dict) -> dict:
        return {
            "data": {
                "type": "lembrete",
                "count": 1,
                "attrbiutes": dto
            }
        }
