from typing import Optional

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class ConfigDataBase(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    DB_ECHO_LOG: bool = False

    @property
    def database_url(self) -> Optional[PostgresDsn]:
        return (
            f"mysql+asyncmy://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings_db = ConfigDataBase(POSTGRES_USER="root",POSTGRES_PASSWORD= "azik959595",POSTGRES_HOST= 'localhost',POSTGRES_PORT= '3306', POSTGRES_DB="social")
