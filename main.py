import asyncio
import os
#os.system("python -m pip install -r requirements.txt")
import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord.ext import tasks, commands
import sys
from secret import TOKEN

guild=None
intents = discord.Intents.all()
application_id = 953037549390151690
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None, case_insensitive=True)

MY_GUILD1 = discord.Object(id=863147923171835925)  # first guild id
MY_GUILD2 = discord.Object(id=811572074719739904)  # second guild id
MY_GUILD3 = discord.Object(id=1066707580459692106)



async def setup_hook():
    bot.tree.copy_global_to(guild=MY_GUILD1)
    await bot.tree.sync(guild=MY_GUILD1)
    await bot.tree.sync(guild=None)
    bot.tree.copy_global_to(guild=MY_GUILD2)
    await bot.tree.sync(guild=MY_GUILD2)
    await bot.tree.sync(guild=None)
    bot.tree.copy_global_to(guild=MY_GUILD3)
    await bot.tree.sync(guild=MY_GUILD3)
    await bot.tree.sync(guild=None)
bot.setup_hook = setup_hook

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f"{bot.command_prefix}help"))
        
    print("Bot is online!")

async def load():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        await bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0x01f121)
    await ctx.send(embed=embed)

async def main():
    await load()
    await bot.start(TOKEN)

    


asyncio.run(main())