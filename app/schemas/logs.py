from datetime import datetime

from pydantic import BaseModel


class LogCreateRequest(BaseModel):
    log: str


class LogResponse(BaseModel):
    id: int
    created: datetime
    ip: str
    method: str
    uri: int
    status_code: int

    class Config:
        orm_mode = True
