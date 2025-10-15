from logging import basicConfig, getLogger
from .utils import assert_getenv

logger = getLogger(__name__)
basicConfig()

DEV_MODE: bool = bool(int(assert_getenv("DEV_MODE")))
SQLALCHEMY_URL: str = (
    f"\
postgresql+psycopg://\
{assert_getenv("POSTGRES_USER")}:{assert_getenv("POSTGRES_PASSWORD")}\
@\
{assert_getenv("POSTGRES_IP")}:{assert_getenv("POSTGRES_PORT")}\
/\
{assert_getenv("POSTGRES_DB")}"
)
NATS_URL: str = f"http://{assert_getenv("NATS_IP")}:{assert_getenv("NATS_PORT")}"
TEST_GUILDS: list[int] = [
    int(id) if id else None for id in assert_getenv("TEST_GUILDS").rstrip().split(",")
]

logger.info("PMBot config loaded")
