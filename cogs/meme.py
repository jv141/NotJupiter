import discord
import random
import aiohttp
from discord.ext import commands

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme', help='Sends a meme')
    async def meme(self, ctx):
        embed = discord.Embed(title="A Random Bad Meme  <:kermit:1070785312399310981>", description="")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                embed.set_footer(text="this meme is so funny. i forgot to laugh 😐")
                await ctx.send(embed=embed)

    @commands.command(name='bubblewrap')
    async def bubblewrap(self, ctx):
        embed=discord.Embed(title="BUBBLEWRAP!")
        embed.add_field(name="", value="||pop||||pop||||pop||||pop||||pop||||pop||||pop||", inline=False)
        embed.add_field(name="", value="||pop||||pop||||pop||||pop||||pop||||pop||||pop||", inline=False)
        embed.add_field(name="", value="||pop||||pop||||pop||||pop||||pop||||pop||||pop||", inline=False)
        embed.add_field(name="", value="||pop||||pop||||pop||||pop||||pop||||pop||||pop||", inline=False)
        embed.add_field(name="", value="||pop||||pop||||pop||||pop||||pop||||pop||||pop||", inline=False)
        embed.add_field(name="", value="||pop||||pop||||pop||||pop||||pop||||pop||||pop||", inline=False)
        embed.add_field(name="", value="||pop||||pop||||pop||||pop||||pop||||pop||||pop||", inline=False)
        await ctx.send(embed=embed)


async def setup(bot):
  await bot.add_cog(Meme(bot))

