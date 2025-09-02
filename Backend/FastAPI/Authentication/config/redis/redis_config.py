from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()

class RedisConfig(BaseSettings):

    HOST: str
    PORT: str
    PASSWORD: str
    DECODE: bool = True

redis_helper = RedisConfig()