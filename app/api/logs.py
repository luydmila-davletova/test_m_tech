from http.client import HTTPException

from fastapi import APIRouter

from app.crud.logs import create_logs, get_all_logs
from app.schemas.logs import LogCreateRequest

router = APIRouter()


@router.post('/api/data/')
async def create_new_log(logs: LogCreateRequest):
    new_log = await create_logs(logs)
    return new_log


@router.get("/api/data/")
async def read_logs():
    try:
        logs = await get_all_logs()
        return logs
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
