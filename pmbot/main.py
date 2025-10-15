from disnake.ext.commands import InteractionBot
from disnake import Intents

from core import TEST_GUILDS, DEV_MODE, assert_getenv

bot = InteractionBot(
    intents=Intents.default(),
    test_guilds=TEST_GUILDS if DEV_MODE else None,
)
bot.run(assert_getenv("BOT_TOKEN"))
