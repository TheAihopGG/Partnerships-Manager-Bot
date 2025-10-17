from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy import select

from models import GuildModel


async def get_guild_by_gid(
    session: AsyncSession,
    *,
    gid: int,
    join_partners: bool = False,
) -> GuildModel | None:
    if join_partners:
        statement = (
            select(GuildModel)
            .options(joinedload(GuildModel.partners))
            .where(GuildModel.id == gid)
        )
    else:
        statement = select(GuildModel).where(GuildModel.id == gid)

    return (await session.execute(statement)).unique().scalar_one_or_none()


async def get_or_create_guild_by_gid(
    session: AsyncSession,
    *,
    gid: int,
    join_partners: bool = False,
) -> GuildModel:
    if guild_model := await get_guild_by_gid(
        session,
        gid=gid,
        join_partners=join_partners,
    ):
        return guild_model
    else:
        guild_model = GuildModel(guild_id=gid)
        session.add(guild_model)
        return guild_model
