import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        """Показывает список доступных команд"""
        embed = discord.Embed(
            title="Список команд",
            description="Используйте префикс `!`",
            color=0x7289DA
        )
        
        commands_list = {
            "🎵 Музыка": "play, stop, pause, resume, skip, queue",
            "🌤 Погода": "погода [город]",
            "🛠 Утилиты": "help"
        }
        
        for category, cmds in commands_list.items():
            embed.add_field(
                name=category,
                value=f"`{cmds}`",
                inline=False
            )
            
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))