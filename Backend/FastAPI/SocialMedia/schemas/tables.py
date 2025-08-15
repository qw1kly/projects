import asyncio

from config.database.database_config import settings_db
from config.database.database_connection import db_helper

from models.models import Base

async def create_tables():
    async with db_helper.engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)

