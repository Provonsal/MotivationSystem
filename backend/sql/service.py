from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .model import *
from sqlalchemy.dialects.postgresql import UUID


async def get_id_by_login(session: AsyncSession, login: str): ->str
    result = await session.execute(select(Passwords.id).where(Passwords.login == login))
    return result


async def get_FIO_by_id(session: AsyncSession, id):
    result = await session.execute(select(Users.firstname, Users.surname, Users.lastname).where(Users.id == id))
    return result


async def get_login(session: AsyncSession, id):
    result = await session.execute(select(Passwords.login).where(Passwords.id == id))
    return result


async def get_hash_password(session: AsyncSession, id):
    result = await session.execute(select(Passwords.hash_pass).where(Passwords.id == id))
    return result


async def get_deals(session: AsyncSession, id):
    result = await session.execute(select(Deals).where(Deals.id == id))
    return result


async def get_salary_and_bonus(user_id: UUID, date: str):
    pass


async def get_rating():
    pass

