from fastapi import APIRouter

from app.crud.logs import create_logs
from app.schemas.logs import LogCreateRequest

router = APIRouter()


@router.post('/api/data/')
async def create_new_log(
        logs: LogCreateRequest,
):
    new_log = await create_logs(logs)
    return new_log
