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


class noobcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.command()
    async def noob(self, ctx):
        # IDs of the two specific users who are allowed to use the command
        allowed_users = [149901535789318145, 175721681975771136]

        # Check if the user is one of the allowed users
        if ctx.author.id not in allowed_users:
            await ctx.send("Sorry, you're not authorized to use this command.")
            return

        # The rest of the command code goes here
        embed = discord.Embed(title="")
        embed.set_author(name="NOOB!")
        embed.add_field(name="", value="<a:laugh:1068475227069222932> <:palpi:1070785387733188690> <:skeletor:1070785436286451872>", inline=False)
        embed.set_image(url='https://t4.ftcdn.net/jpg/04/75/40/63/360_F_475406303_p5NYVLEHoMuFKZYSTvofu5NTkbZliLi0.jpg')
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(noobcog(bot))
