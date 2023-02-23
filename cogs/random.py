import discord
import random
import aiohttp
from discord.ext import commands
import requests
import asyncio
import textwrap
import urllib
import datetime
import io
from io import BytesIO

class randomcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='joke')
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get("https://official-joke-api.appspot.com/random_joke")
            response = await request.json()
    
            setup = response["setup"]
            punchline = response["punchline"]
    
            embed = discord.Embed(title="Here's a random joke for you! <:kermit:1070785312399310981>", color=discord.Color.purple())
            embed.add_field(name="Setup:", value=setup, inline=False)
            embed.add_field(name="Punchline:", value=punchline, inline=False)
            await ctx.send(embed=embed)


    @commands.command()
    async def avatar(self, ctx, user: discord.User = None):
        if user is None:
            await ctx.send("Please specify a user.")
            return
        # f'https://some-random-api.ml/canvas/overlay/comrade?avatar={member.avatar_url_as(format="png")}'
        embed=discord.Embed(title="")
       # embed.add_field(name="a", value="e", inline=False)
        embed.set_author(name=f"{user.name}'s Avatar")
        embed.set_image(url=user.avatar)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(randomcog(bot))
