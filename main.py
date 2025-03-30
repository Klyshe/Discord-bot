import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv() 

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def setup():
    await bot.load_extension('cogs.music_cog')
    await bot.load_extension('cogs.weather_cog')
    await bot.load_extension('cogs.events_cog')
    await bot.load_extension('cogs.help_cog')

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} готов!') 

async def main():
    await setup()
    await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())