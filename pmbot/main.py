from disnake.ext.commands import InteractionBot
from disnake import Intents

from core import TEST_GUILDS, DEV_MODE, assert_getenv
from cogs import help, partnerships, settings

bot = InteractionBot(
    intents=Intents.default(),
    test_guilds=TEST_GUILDS if DEV_MODE else None,
)
[
    bot.add_cog(cog)
    for cog in {
        help.HelpCog(),
        partnerships.PartnershipsCog(),
        settings.SettingsCog(),
    }
]
bot.run(assert_getenv("BOT_TOKEN"))
