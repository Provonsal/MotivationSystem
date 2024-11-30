import os
from dotenv import load_dotenv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from typing import Annotated
from fastapi import Depends

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


USER_DATABASE = os.getenv('USER_DATABASE')
PASS_DATABASE = os.getenv('PASS_DATABASE')
NAME_DATABASE = os.getenv('NAME_DATABASE')
HOST_DATABASE = os.getenv('HOST_DATABASE')
PORT_DATABASE = os.getenv('PORT_DATABASE')
URL_DATABASE = f'postgresql+asyncpg://{USER_DATABASE}:{PASS_DATABASE}@{HOST_DATABASE}:{PORT_DATABASE}/{NAME_DATABASE}'

engine = create_async_engine(URL_DATABASE, echo=True)
Base = declarative_base()
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

db_dependency = Annotated[AsyncSession, Depends(get_session)]