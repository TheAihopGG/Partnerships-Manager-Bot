from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from logging import getLogger

from .config import SQLALCHEMY_URL

logger = getLogger(__name__)
engine = create_async_engine(SQLALCHEMY_URL)
sessionmaker = async_sessionmaker(engine, autoflush=True)
