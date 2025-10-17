from sqlalchemy import func
from sqlalchemy.orm import declared_attr, Mapped, mapped_column
from sqlalchemy.types import BigInteger
from datetime import datetime


class IDMixin:
    @declared_attr
    def id(cls: type[IDMixin]) -> Mapped[int]:
        return mapped_column(
            BigInteger(),
            primary_key=True,
            index=True,
        )


class CreatedAtMixin:
    @declared_attr
    def created_at(cls: type[CreatedAtMixin]) -> Mapped[datetime]:
        return mapped_column(
            default=func.now(),
            nullable=False,
        )


class UpdatedAtMixin:
    @declared_attr
    def created_at(cls: type[UpdatedAtMixin]) -> Mapped[datetime]:
        return mapped_column(
            default=func.now(),
            onupdate=datetime.now,
            nullable=False,
        )
