import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

# Настройка интентов
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

# Загрузка когов
async def setup():
    await bot.load_extension('cogs.music_cog')
    await bot.load_extension('cogs.weather_cog')
    await bot.load_extension('cogs.events_cog')

# Запуск бота
async def main():
    await setup()
    await bot.start(os.getenv('TOKEN'))

if __name__ == "__main__":
    asyncio.run(main())