from sqlalchemy import ForeignKey, DECIMAL, String, DATETIME, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime

from .base import Base




class Users(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    firstname: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))

    password: Mapped["Passwords"] = relationship(
        "Passwords",
        back_populates="user",
        uselist=False,
        # lazy="joined"
    )

    balance: Mapped["Balance"] = relationship(
        "Balance",
        back_populates="user",
        uselist=False,\
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
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True, default=uuid4())
    hash_pass: Mapped[str] = mapped_column(String(64))
    login: Mapped[str] = mapped_column(String(30))

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="password",
    )

    def __repr__(self) -> str:
        return f"Passwords(id={self.id!r}, login={self.login!r}, hash_pass={self.hash_pass!r})"


class Balance(Base):
    __tablename__ = "balance"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True, default=uuid4())
    money: Mapped[str] = mapped_column(DECIMAL(10, 2))

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="balance",
    )

    def __repr__(self) -> str:
        return f"Balance(id={self.id!r}, money={self.money!r}"


class Deals(Base):
    __tablename__ = "deals"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_user: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    sum: Mapped[str] = mapped_column(DECIMAL(10, 2))
    percent: Mapped[str] = mapped_column(DECIMAL(10, 2))
    date_deal_start: Mapped[datetime] = mapped_column(DATETIME)
    date_deal_end: Mapped[datetime] = mapped_column(DATETIME)
    selled: Mapped[str] = mapped_column(String(30))
    count: Mapped[int] = mapped_column(Integer)
    # is_cost: Mapped[bool] =

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="deal",
    )

    def __repr__(self) -> str:
        return f"Balance(id={self.id!r}, sum={self.sum!r}, percent={self.percent!r}, money={self.sum!r}, money={self.sum!r}"

