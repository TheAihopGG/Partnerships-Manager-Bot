from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from .config import SQLALCHEMY_URL

engine = create_async_engine(SQLALCHEMY_URL)
sessionmaker = async_sessionmaker(engine)
