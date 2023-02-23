import json
import random
import discord
from discord.ext import commands

class Crime(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("crime_responses.json", "r") as f:
            self.crime_responses = json.load(f)
  
    async def open_account(self, user):
        with open("mainbank.json", "r") as f:
            users = json.load(f)

        if str(user.id) not in users:
            users[str(user.id)] = {}
            users[str(user.id)]["cash"] = 0
            users[str(user.id)]["bank"] = 0

            with open("mainbank.json", "w") as f:
                json.dump(users, f)

    async def get_bank_data(self):
        with open("mainbank.json", "r") as f:
            users = json.load(f)

        return users
        

    @commands.command()
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def crime(self, ctx):
        await self.open_account(ctx.author)
        users = await self.get_bank_data()
        user = ctx.author
        success_rate = 0.6
        if users[str(user.id)]["cash"] < 250:
            await ctx.send("you need 250 cash to pay for the tools to commit a crime (NO YOU CAN'T STEAL THE TOOLS)")
            return
        if random.random() < success_rate:
            earnings = random.randrange(50, 1500)
            response = random.choice(self.crime_responses['success'])
            description = response.format(earnings)
            em = discord.Embed(title="", description=description, color=0x3fab62)
            em.set_author(name=f"{user.name}'s  Crime Results", icon_url=user.avatar)
            await ctx.send(embed=em)
            users[str(user.id)]["cash"] += earnings
        else:
            loss = random.randrange(250)
            response = random.choice(self.crime_responses['fail'])
            description = response.format(loss)
            em = discord.Embed(title="", description=description, color=0xd2171c)
            em.set_author(name=f"{user.name}'s  Crime Results", icon_url=user.avatar)
            await ctx.send(embed=em)
            users[str(user.id)]["cash"] -= loss
    
        with open("mainbank.json","w") as f:
            json.dump(users,f)

    @crime.error
    async def crime_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(int(error.retry_after), 60)
            hours, minutes = divmod(minutes, 60)
            em = discord.Embed(title=f"Slowdown bruh",description=f"You can comit another crime in {hours} hours, {minutes} minutes, and {seconds} seconds.",color=0xd2171c)
            await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(Crime(bot))
