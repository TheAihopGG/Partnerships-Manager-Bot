from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import CreatedAtMixin, UpdatedAtMixin, IDMixin

if TYPE_CHECKING:
    from .partner import PartnerModel


class GuildModel(
    Base,
    IDMixin,
    CreatedAtMixin,
    UpdatedAtMixin,
):
    __tablename__ = "guilds"
    guild_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    prm_role_id: Mapped[int] = mapped_column(nullable=True)
    partners: Mapped[List[PartnerModel]] = relationship("PartnerModel",back_populates="partner_guild",foreign_keys="PartnerModel.partner_id")
