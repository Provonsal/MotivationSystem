import datetime
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from sql.base import init_models
from .model import *
from sqlalchemy.dialects.postgresql import UUID

import json


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


async def insert_test_data(session: AsyncSession):
    from table_data import data

    # Загрузка данных из JSON

    # file_path = "table_data.json"
    #
    # with open(file_path, "r") as json_file:
    #     data = json.load(json_file)

    # Добавление пользователей

    users = [
        Users(
            id=user["id"],
            firstname=user["firstname"],
            surname=user["surname"],
            lastname=user["lastname"]
        )
        for user in data["users"]
    ]
    session.add_all(users)

    # Добавление паролей
    passwords = [
        Passwords(
            id=password["id"],
            login=password["login"],
            hash_pass=password["hash_pass"]
        )
        for password in data["passwords"]
    ]
    session.add_all(passwords)

    # Добавление баланса
    balances = [
        Balance(
            id=balance["id"],
            money=Decimal(balance["money"])
        )
        for balance in data["balance"]
    ]
    session.add_all(balances)

    # Добавление сделок
    deals = [
        Deals(
            id=deal["id"],
            id_user=deal["id_user"],
            sum=Decimal(deal["sum"]),
            percent=Decimal(deal["percent"]),
            date_deal_start=datetime.fromisoformat(deal["date_deal_start"]),
            date_deal_end=datetime.fromisoformat(deal["date_deal_end"]),
            selled=deal["selled"],
            count=deal["count"]
        )
        for deal in data["deals"]
    ]

    session.add_all(deals)

    # Коммитим изменения
    await session.commit()


async def get_rating():
    pass

