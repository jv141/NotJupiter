import discord
from discord.ext import commands
import random

class PatchNote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.patch_notes = [
            "Increased global temperature by 2 degrees Celsius.",
            "Added 20 new species of insects.",
            "Rebalanced the ecosystem.",
            "Reduced plastic waste by 50%.",
            "Introduced new strain of virus.",
            "Removed ozone layer.",
            "Decreased deforestation by 30%.",
            "Improved air quality in major cities.",
            "Added more oil reserves.",
            "Implemented new technology to combat climate change.",
            "Increased sea levels by 1 meter.",
            "Fixed a bug where certain species were overpopulating.",
            "Introduced new renewable energy sources.",
            "Added 5 new natural disasters.",
            "Improved soil quality for farming.",
            "Decreased biodiversity.",
            "Implemented stricter regulations on industrial waste.",
            "Increased water pollution.",
            "Improved ocean biodiversity.",
            "Added more protected areas for wildlife.",
            "Reduced the size of mosquitoes and other annoying insects by 50%",
            "Fixed a bug where Joppe accidentally had rights"
        ]
        
    @commands.command()
    async def patchnote(self, ctx):
        patch_note = random.choice(self.patch_notes)
        em = discord.Embed(title="Earth Patch Note", description=patch_note, color=0x3fab62)
        await ctx.send(embed=em)

      
async def setup(bot):
    await bot.add_cog(PatchNote(bot))