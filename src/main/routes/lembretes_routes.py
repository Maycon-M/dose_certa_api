from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from src.controllers.http_types.http_request import HttpRequest

from src.main.composer.criar_lembrete_composer import criar_lembrete_composer
from src.main.composer.listar_por_id_composer import listar_por_id_composer
from src.main.composer.listar_todos_composer import listar_todos_composer
from src.main.composer.atualizar_lembrete_composer import atualizar_lembrete_composer
from src.main.composer.deletar_lembrete_composer import deletar_lembrete_composer

router = APIRouter(
    prefix="/lembretes",
    tags=["lembretes"],
    responses={
        200: {"description": "OK"},
        201: {"description": "Created"},
        204: {"description": "No Content"},
        400: {"description": "Bad Request"},
        404: {"description": "Not found"},
        422: {"description": "Unprocessable Entity"},
        500: {"description": "Internal Server Error"}}
)

@router.post("/novo/")
async def criar_lembrete(request: Request):
    try:
        body = await request.json()
        
        http_request = HttpRequest(body)
        controller = criar_lembrete_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}")
async def listar_lembretes(id: int):
    try:
        http_request = HttpRequest(param={"id": id})
        controller = listar_por_id_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/")
async def listar_todos_lembretes():
    try:
        http_request = HttpRequest()
        controller = listar_todos_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{id}")
async def atualizar_lembrete(id: int, request: Request):
    try:
        body = await request.json()
        
        http_request = HttpRequest(param={"id": id}, body=body)
        controller = atualizar_lembrete_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{id}")
async def deletar_lembrete(id: int):
    try:
        http_request = HttpRequest(param={"id": id})
        controller = deletar_lembrete_composer()
        http_respose = controller.handle(http_request)
        return JSONResponse(status_code=http_respose.status_code, content=http_respose.body)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
