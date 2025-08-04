from typing import Optional

from pydantic import MYSQLDsn
from pydantic_settings import BaseSettings


class ConfigDataBase(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: str
    MYSQL_DB: str
    DB_ECHO_LOG: bool = False

    @property
    def database_url(self) -> Optional[MYSQLDsn]:
        return (
            f"mysql+asyncmy://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@"
            f"{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )


settings_db = ConfigDataBase(MYSQL_USER="",MYSQL_PASSWORD= "",MYSQL_HOST= '',MYSQL_PORT= '', MYSQL_DB="social")

