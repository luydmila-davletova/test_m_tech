from typing import List

from sqlalchemy import select

from app.core.db import AsyncSessionLocal
from app.models.logs import Log
from app.schemas.logs import LogCreateRequest


async def create_logs(
        new_log: LogCreateRequest
) -> Log:
    try:
        log_data = new_log.log.split(" ")
        if len(log_data) != 4:
            raise ValueError(
                "Лог должен содержать ровно 4 элемента: IP адрес, HTTP метод, URI, код статуса"
            )

        ip_address, http_method, uri, status_code = log_data
        log = Log(
            ip_address=ip_address,
            http_method=http_method,
            uri=uri,
            status_code=int(status_code)
        )

        async with AsyncSessionLocal() as session:
            session.add(log)
            await session.commit()
            await session.refresh(log)
        return log
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
        raise e


async def get_all_logs() -> List[Log]:
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Log))
        logs_list = result.scalars().all()
    return logs_list
