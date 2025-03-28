import discord
from discord.ext import commands
import aiohttp
import os

class WeatherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.weather_icons = {
            "clear": "☀️ Ясно",
            "clouds": "☁️ Облачно",
            "rain": "🌧 Дождь",
            "snow": "❄️ Снег",
            "thunderstorm": "⛈ Гроза",
            "mist": "🌫 Туман"
        }

    @commands.command(name="погода")
    async def weather(self, ctx, *, city: str):
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "ru"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(base_url, params=params) as response:
                    data = await response.json()

                    if data["cod"] != 200:
                        return await ctx.send("🚫 Город не найден или ошибка API")

                   
                    main = data["main"]
                    weather = data["weather"][0]
                    wind = data["wind"]
                    sys = data["sys"]

                
                    weather_type = weather["main"].lower()
                    icon_data = self.weather_icons.get(weather_type, "🌤️")
                    icon, status = icon_data.split() if " " in icon_data else ("🌤️", "Нормально")

                   
                    embed = discord.Embed(
                        title=f"{icon} Погода в {data['name']}, {sys['country']}",
                        color=0x00ff00 if "ясно" in status.lower() else 0x7289DA
                    )
                    
                    embed.add_field(name="🌡 Температура", value=f"{main['temp']}°C", inline=True)
                    embed.add_field(name="💨 Ощущается как", value=f"{main['feels_like']}°C", inline=True)
                    embed.add_field(name="💧 Влажность", value=f"{main['humidity']}%", inline=True)
                    embed.add_field(name="🌬 Ветер", value=f"{wind['speed']} м/с", inline=True)
                    embed.add_field(name="📝 Состояние", value=weather["description"].capitalize(), inline=True)
                    embed.set_thumbnail(url=f"http://openweathermap.org/img/wn/{weather['icon']}@2x.png")
                    embed.set_footer(text="Данные предоставлены OpenWeatherMap")

                    await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"⚠️ Ошибка: {str(e)}")

async def setup(bot):
    await bot.add_cog(WeatherCog(bot))