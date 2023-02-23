import discord
from discord.ext import commands

class helpcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='help')
    async def help_command(self, ctx):
       # commands_list = []
        #for command in self.bot.commands:
           # commands_list.append(command.name)
       # embed = discord.Embed(title="Jupiter bot's Help Menu", description=f'List of available commands: {", ".join(commands_list)}')
       # await ctx.send(embed=embed)

        embed=discord.Embed(title="Jupiter Bot's Help Menu", color=0xff8000)
        embed.add_field(name="Economy", value="work, beg, crime, store, buy, sell, use, bag, balance, pay, rob, leaderboard, withdraw, deposit", inline=True)
        embed.add_field(name="Gamble", value="slots, blackjack, lottery, race, racers", inline=True)
        embed.add_field(name="Fun", value="8ball, meme, bubblewrap, fight", inline=True)
        embed.add_field(name="Other", value="weather, invite, serverinvite, userinfo, serverinfo", inline=True)
        await ctx.send(embed=embed)


async def setup(bot):
  await bot.add_cog(helpcmd(bot))

