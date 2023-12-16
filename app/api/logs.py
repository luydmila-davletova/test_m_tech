from http.client import HTTPException

from fastapi import APIRouter

from app.crud.logs import create_logs, get_all_logs
from app.schemas.logs import LogCreateRequest

router = APIRouter()


@router.post('/api/data/')
async def create_new_log(logs: LogCreateRequest):
    """Эндпоинт для создания логов."""
    try:
        new_log = await create_logs(logs)
        return new_log
    except Exception:
        raise HTTPException(status_code=418, detail="Что то пошло не так")


@router.get("/api/data/")
async def read_all_logs():
    """Эндпоинт для чтения логов."""
    try:
        logs = await get_all_logs()
        return logs
    except Exception:
        raise HTTPException(status_code=418, detail="Что то пошло не так")
