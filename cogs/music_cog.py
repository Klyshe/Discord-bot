import discord
from discord.ext import commands
import youtube_dl

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.music_queue = []
        self.is_playing = False
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    @commands.command()
    async def play(self, ctx, url):
        voice_channel = ctx.author.voice.channel
        if not voice_channel:
            await ctx.send("Сначала подключитесь к голосовому каналу!")
            return
        
        voice_client = await voice_channel.connect()
        
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            
        voice_client.play(discord.FFmpegPCMAudio(url2))
        self.is_playing = True
        await ctx.send(f"Сейчас играет: {info['title']}")

    @commands.command()
    async def stop(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client.is_playing():
            voice_client.stop()
        await voice_client.disconnect()
        await ctx.send("Воспроизведение остановлено")

async def setup(bot):
    await bot.add_cog(MusicCog(bot))