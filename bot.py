import os
import hikari
import lightbulb
import aiohttp
from env import *

bot = lightbulb.BotApp(
    help_slash_command=True,
    token=DISCORD_TOKEN,
    intents=hikari.Intents.ALL,
)

bot.load_extensions_from('extensions')

# Start the bot and aiohttp session
@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
    print('WhiskerWise has started')
    bot.d.aio_session = aiohttp.ClientSession()

# When the bot closes, close the aiohttp session
@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    print('WhiskerWise is closing')
    bot.d.aio_session.close()

if __name__ == "__main__":
    bot.run()