import discord
from discord.ext import commands

class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Бот {self.bot.user.name} готов к работе!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
       
        if message.content.lower() == 'привет':
            await message.channel.send(f'Привет, {message.author.mention}!')
        
        elif message.content.lower() == 'пока':
            await message.channel.send('До свидания!')
        
        
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(EventsCog(bot))