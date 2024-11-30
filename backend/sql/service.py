from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from model import *


async def get_id_by_login(session: AsyncSession, login):
    result = await session.execute(select(Passwords.id).where(Passwords.login == login))
    return result


def get_FIO_by_id(session: AsyncSession, id):
    result = await session.execute(select(Users.firstname, Users.surname, Users.lastname).where(Users.id == id))
    return result


def get_login(session: AsyncSession, id):
    result = await session.execute(select(Passwords.login).where(Passwords.id == id))
    return result


def get_hash_password(session: AsyncSession, id):
    result = await session.execute(select(Passwords.hash_pass).where(Passwords.id == id))
    return result

