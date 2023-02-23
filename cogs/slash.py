import time
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord.ext.commands import Bot
import random
import os
import discord
from discord.ext import commands
import asyncio
import requests
import json
from discord.utils import get
from discord.utils import find
import datetime



class slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def pong(self, ctx):
        yo = round(self.bot.latency * 1000)
        embed = discord.Embed(title="Ping! :ping_pong:", color=discord.Color.random())
        embed.add_field(name="Latency:", value=f"{yo}ms")
        await ctx.send(embed=embed)
    

    @app_commands.command(name="ping", description="test the latency")
    async def ping(self, interaction: discord.Interaction):
        yo = round(self.bot.latency * 1000)
        embed = discord.Embed(title="Pong! :ping_pong:", color=discord.Color.random())
        embed.add_field(name="Latency:", value=f"{yo}ms")
        await interaction.response.send_message(embed=embed)
  

    @app_commands.command(name="testing", description="what are you testing?")
    async def testing(self, interaction: discord.Interaction, testing:str):
        await interaction.response.send_message(f"We are now testing: {testing}")

async def setup(bot):
    await bot.add_cog(slash(bot))