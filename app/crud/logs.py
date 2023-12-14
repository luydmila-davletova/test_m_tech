from typing import List

from sqlalchemy import select

from app.core.db import AsyncSessionLocal
from app.models.logs import Log
from app.schemas.logs import LogCreateRequest


async def create_logs(
        new_log: LogCreateRequest
) -> Log:
    log_data = new_log.log.split(" ")
    ip_address, http_method, uri, status_code = log_data

    # Создание объекта лога для сохранения в базу данных
    log = Log(
        ip_address=ip_address,
        http_method=http_method,
        uri=uri,
        status_code=int(status_code)
    )

    async with AsyncSessionLocal() as session:
        # Добавляем созданный объект в сессию.
        session.add(log)

        # Записываем изменения непосредственно в БД.
        await session.commit()

        await session.refresh(log)
    return log


async def get_all_logs() -> List[Log]:
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Log))
        logs_list = result.scalars().all()
    return logs_list
