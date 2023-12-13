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
        # Никакие действия с базой пока ещё не выполняются.
        session.add(log)

        # Записываем изменения непосредственно в БД.
        # Так как сессия асинхронная, используем ключевое слово await.
        await session.commit()

        # Обновляем объект db_room: считываем данные из БД, чтобы получить его id.
        await session.refresh(log)
    # Возвращаем только что созданный объект класса MeetingRoom.
    return log