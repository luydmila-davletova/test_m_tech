from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime

from app.core.db import Base


class Log(Base):
    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, index=True)
    http_method = Column(String)
    uri = Column(String)
    status_code = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
