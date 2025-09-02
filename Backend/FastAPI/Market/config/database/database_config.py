from typing import Optional

from pydantic import MySQLDsn
from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()

class ConfigDataBase(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: str
    MYSQL_DB: str
    DB_ECHO_LOG: bool = False

    @property
    def database_url(self) -> Optional[MySQLDsn]:
        return (
            f"mysql+asyncmy://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@"
            f"{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        )


settings_db = ConfigDataBase()
