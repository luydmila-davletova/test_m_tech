
from fastapi import FastAPI


from app.api.logs import router
from app.core.config import settings

app = FastAPI(title=settings.app_title)

app.include_router(router)

