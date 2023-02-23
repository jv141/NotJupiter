import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

class poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

  
    @commands.command(name='poll', hidden=True)
    @commands.has_permissions(administrator=True)
    async def poll(self, ctx, *, content:str):
        print("Creating yes/no poll...")
        #create the embed file
        embed = discord.Embed(
          title=f"{content}",
          description="React to this message with ✅ for yes, or with ❌ for no.",
          color=0x00ff00)
    #set the author and icon
        embed.set_author(name="POLL: ")
        print("Embed created")
    #send the embed
        message = await ctx.message.delete()
        message = await ctx.channel.send(embed=embed)
    #add the reactions
        await message.add_reaction("✅")
        await message.add_reaction("❌")
   

    @poll.error
    async def poll_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")


  
    @commands.command(name='announce', aliases=['an', 'kondig'])
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *, content:str):
        #create the embed file
        embed = discord.Embed(
          title=f"{content}",
          color=0x332da6)
    #set the author and icon
        embed.set_author(name="JupiterBot Announcement: ")
        #print("Embed created")
    #send the embed
        message = await ctx.message.delete()
        message = await ctx.channel.send(embed=embed)
    
   

    @announce.error
    async def announce_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @say.error
    async def say_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")

   
######
    @commands.command(name='multipoll', hidden=True)
    @commands.has_permissions(administrator=True)
    async def multipoll(self, ctx, *, content:str):
        print("Creating yes/no poll...")
        #create the embed file
        embed = discord.Embed(
          title=f"{content}",
          description="React to this message with the option you'd like.",
          color=0x00ff00)
    #set the author and icon
        embed.set_author(name="POLL: ")
        print("Embed created")
    #send the embed
        message = await ctx.message.delete()
        message = await ctx.channel.send(embed=embed)
    #add the reactions
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")

    @multipoll.error
    async def multipoll_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")
  
async def setup(bot):
  await bot.add_cog(poll(bot))
