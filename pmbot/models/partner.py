from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, IDMixin

if TYPE_CHECKING:
    from .guild import GuildModel


class PartnerModel(
    Base,
    IDMixin,
    CreatedAtMixin,
    UpdatedAtMixin,
):
    __tablename__ = "partners"
    host_id: Mapped[int] = mapped_column(nullable=False)
    partner_id: Mapped[int] = mapped_column(ForeignKey("guilds.id"), nullable=False)
    partner_guild: Mapped[GuildModel] = relationship(
        "GuildModel",
        foreign_keys=[partner_id],
        back_populates="partners",
    )
    __table_args__ = (UniqueConstraint(host_id, partner_id),)
