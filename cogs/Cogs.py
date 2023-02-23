import discord
from discord.ext import commands

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cogs', aliases=['extensions'])
    @commands.is_owner()
    async def view_cogs(self, ctx):
        """View all the cogs that are currently loaded in the bot."""
        cogs = [cog.__class__.__name__ for cog in self.bot.cogs.values()]
        embed = discord.Embed(
            title='Cogs',
            description=f'The following cogs are currently loaded: {", ".join(cogs)}',
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)    
    
async def setup(bot):
    await bot.add_cog(Cogs(bot))