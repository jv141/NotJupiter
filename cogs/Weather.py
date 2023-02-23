import discord
import random
import aiohttp
from discord.ext import commands
import requests
import asyncio

api_key = "b155eaffda6909c08f61d796c6824d41"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='weather', help='Shows the weather')
    async def weather(self, ctx, city):
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsius = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
            color=0x22888d,
            timestamp=ctx.message.created_at,)
            embed.add_field(name="Description", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsius}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.pinimg.com/originals/30/c7/1d/30c71d7df427edef6bfc13839060dc02.gif")
            embed.set_footer(text=f"Requested by {ctx.author.name}")

            await channel.send(embed=embed)
        else:
            await channel.send("City not found.")

async def setup(bot):
  await bot.add_cog(weather(bot))

