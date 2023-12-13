from pydantic import BaseSettings

# DATABASE_URL = "postgresql://user:password@localhost/dbname"


class Settings(BaseSettings):
    app_title: str = 'web app'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()