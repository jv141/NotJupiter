import json
import random
import discord
from discord.ext import commands

class Adventure(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.story = "Once upon a time, there was a brave knight who set out on a quest to defeat a fierce dragon that had been terrorizing the kingdom. As the knight journeyed through the forest, they came across a fork in the road. One path led to (1) the dragon's lair, the other led to (2) a mystical castle, and the third path is to (3) turn around and go home. Which path will the knight choose? [type 1, 2 or 3]"
        self.options = ["1", "2", "3"]
    @commands.command()
    async def adventure(self, ctx):
        await ctx.send(self.story)
        response = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        if response.content in self.options:
            if response.content == "1":
                await ctx.send("The knight chooses the path to the dragon's lair. They fought a fierce battle, but ultimately emerged victorious. The dragon's hoard of treasure was theirs for the taking. Do you want to take the treasure or leave it?")
                response = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                if response.content == "take it":
                    await ctx.send("The knight takes the treasure and becomes rich, but the weight of guilt for taking it weighs heavy on them. They eventually leave their riches and become a wandering hermit.")
                else:
                    await ctx.send("The knight leaves the treasure and becomes a true hero in the eyes of the kingdom, living a life of honor and respect.")
            elif response.content == "2":
                await ctx.send("The knight chooses the path to the mystical castle. Inside, they found a powerful magic sword, which they used to defeat the dragon and save the kingdom. The knight was offered a choice to stay in the castle and become the ruler or return to their normal life. Do you want to stay or return home ?")
                response = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
                if response.content == "stay":
                    await ctx.send("The knight chooses to stay and becomes a wise and just ruler, leading the kingdom to a golden age.")
                else:
                    await ctx.send("The knight chooses to return home and live a peaceful life, becoming a legend through stories and songs.")
            else:
                await ctx.send("The knight just turned around and went back home to sleep")
        else:
            await ctx.send("Invalid option. Please type either '1', '2' or '3'.")

async def setup(bot):
    await bot.add_cog(Adventure(bot))