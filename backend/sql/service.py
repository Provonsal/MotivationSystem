from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .model import *
from sqlalchemy.dialects.postgresql import UUID


async def get_id_by_login(session: AsyncSession, login: str) -> str:
    result = await session.execute(select(Passwords.id).where(Passwords.login == login))
    return result.scalars().one()


async def get_FIO_by_id(session: AsyncSession, id: UUID) -> dict:
    result = await session.execute(select(Users.firstname, Users.surname, Users.lastname).where(Users.id == id))
    return result.scalars().one()


async def get_login(session: AsyncSession, id: UUID) -> str:
    result = await session.execute(select(Passwords.login).where(Passwords.id == id))
    return result.scalars().one()


async def get_hash_password(session: AsyncSession, id: UUID) -> str:
    result = await session.execute(select(Passwords.hash_pass).where(Passwords.id == id))
    return result.scalars().one()


async def get_deals(session: AsyncSession, id: UUID) -> list[dict]:
    result = await session.execute(select(Deals).where(Deals.id == id))
    return result.scalars().all()


async def get_salary_and_bonus(user_id: UUID, date: str):
    pass


async def get_rating():
    pass

