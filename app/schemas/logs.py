import re
from datetime import datetime

from pydantic import BaseModel, validator


class LogCreateRequest(BaseModel):
    log: str

    @validator('log')
    def validate_log_format(cls, v):
        pattern = re.compile(r"(\S+) (\S+) (\S+) (\d+)")
        if not pattern.fullmatch(v):
            raise ValueError("Некорректный формат лога")
        return v


class LogResponse(BaseModel):
    id: int
    created: datetime
    ip: str
    method: str
    uri: int
    status_code: int

    class Config:
        orm_mode = True
