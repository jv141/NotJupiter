import json
import random
import discord
from discord.ext import commands

with open('fight_responses.json', 'r') as f:
  fight_results = json.load(f)

class Fight(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("fight_responses.json", "r") as f:
            self.fight_responses = json.load(f)


    @commands.command()
    async def fight(self, ctx, user:str=None, *, weapon:str=None):
        """Fight someone with something"""
        if user is None or user.lower() == ctx.author.mention or user == ctx.author.name.lower() or ctx.guild is not None and ctx.author.nick is not None and user == ctx.author.nick.lower():
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="You did not tag anyone to fight", value="{} fought themself but only ended up in a mental hospital!".format(ctx.author.mention))
            await ctx.send(embed=embed)
            return
        if weapon is None:
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="You didn't select an item to fight with", value="{0} tried to fight {1} with nothing so {1} beat them up".format(ctx.author.mention, user))
            await ctx.send(embed=embed)
            return
        embed=discord.Embed(color=0xff80ff)
        embed.add_field(name="Fight Results", value="{} used **{}** on **{}** {}".format(ctx.author.mention, weapon, user, random.choice(fight_results).replace("%user%", user).replace("%attacker%", ctx.author.mention)))
        await ctx.send(embed=embed)



    
      
async def setup(bot):
    await bot.add_cog(Fight(bot))