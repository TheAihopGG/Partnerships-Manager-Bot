from logging import getLogger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from models import GuildModel, PartnerModel

logger = getLogger(__name__)


async def add_partner(
    session: AsyncSession,
    *,
    host_guild_model: GuildModel,
    partner_guild_model: GuildModel,
) -> PartnerModel | None:
    """:return: `PartnerModel` if partner is successfully added, `None` if partner already exists"""
    if not (
        await session.execute(
            select(PartnerModel).where(
                PartnerModel.host_id == host_guild_model.id,
                PartnerModel.partner_id == partner_guild_model.id,
            )
        )
    ).scalar_one_or_none():
        partner_model = PartnerModel(
            host_id=host_guild_model.id,
            partner_id=partner_guild_model.id,
        )
        logger.critical(partner_model.host_id)
        logger.critical(partner_model.partner_id)
        # host_guild_model.partners.append(partner_model)
        session.add(partner_model)
        await session.commit()
        return partner_model


async def remove_partner(
    session: AsyncSession,
    *,
    host_guild_model: GuildModel,
    partner_guild_model: GuildModel,
) -> bool:
    return bool(
        (
            await session.execute(
                delete(PartnerModel).where(
                    PartnerModel.host_id == host_guild_model.id,
                    PartnerModel.partner_id == partner_guild_model.id,
                )
            )
        ).rowcount
    )
