from logging import basicConfig, getLogger
from .utils import assert_getenv

logger = getLogger(__name__)
basicConfig()

DEV_MODE: bool = bool(int(assert_getenv("DEV_MODE")))
SQLALCHEMY_URL: str = (
    f"\
    postgressql+psycopg://\
    {assert_getenv("POSTGRES_USER")}:{assert_getenv("POSTGRES_PASSWORD")}\
    @\
    {assert_getenv("POSTGRES_IP")}:{assert_getenv("POSTGRES_PORT")}\
    /\
    {assert_getenv("POSTGRES_DB")}"
)

logger.info("PMBot config loaded")

__all__ = (
    "DEV_MODE",
    "SQLALCHEMY_URL",
)
