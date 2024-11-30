import os
from dotenv import load_dotenv
from datetime import date
from sqlalchemy import ForeignKey, DECIMAL, String, DATE
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str]

    password: Mapped["Passwords"] = relationship(
        "Passwords",
        back_populates="user",
        uselist=False,
        # lazy="joined"
    )

    balance: Mapped["Balance"] = relationship(
        "Balance",
        back_populates="user",
        uselist=False,
        # lazy="joined"
    )

    deal: Mapped["Deals"] = relationship(
        "Deals",
        back_populates="user",
        uselist=False,
        # lazy="joined"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Passwords(Base):
    __tablename__ = "passwords"
    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    hash_pass: Mapped[str] = mapped_column(String(30))
    login: Mapped[str] = mapped_column(String(30))

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="password",
    )

    def __repr__(self) -> str:
        return f"Passwords(id={self.id!r}, login={self.login!r}, hash_pass={self.hash_pass!r})"


class Balance(Base):
    __tablename__ = "balance"
    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    money: Mapped[str] = mapped_column(DECIMAL(10, 2))

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="balance",
    )

    def __repr__(self) -> str:
        return f"Balance(id={self.id!r}, money={self.money!r}"


class Deals(Base):
    __tablename__ = "deals"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id"))
    sum: Mapped[str] = mapped_column(DECIMAL(10, 2))
    percent: Mapped[str] = mapped_column(DECIMAL(10, 2))
    date_deal_start: Mapped[date] = mapped_column(DATE)
    date_deal_end: Mapped[date] = mapped_column(DATE)

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="deal",
    )

    def __repr__(self) -> str:
        return f"Balance(id={self.id!r}, sum={self.sum!r}, percent={self.percent!r}, money={self.sum!r}, money={self.sum!r}"



