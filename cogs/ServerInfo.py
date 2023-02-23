import discord
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f'{guild.name} Server Info', color=0x00ff00)
        embed.add_field(name='Server ID', value=guild.id)
        #embed.add_field(name='Server Region', value=guild.region)
        embed.add_field(name='Server Creation Date', value=guild.created_at.strftime("%A, %B %d %Y"))
        embed.add_field(name='Server Owner', value=guild.owner.name)
        embed.add_field(name='Server Member Count', value=guild.member_count)
        embed.add_field(name='Server Roles', value=', '.join([role.name for role in guild.roles]))
        embed.add_field(name='Server Channels', value=f'{len(guild.text_channels)} Text Channels and {len(guild.voice_channels)} Voice Channels')
        embed.add_field(name='Server Emoji Count', value=len(guild.emojis))
        embed.add_field(name='Server Boost Count', value=guild.premium_subscription_count)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)


    @commands.command()
    async def userinfo(self, ctx, user: discord.Member):
        embed = discord.Embed(title=f"User Information - {user}", color=0x00ff00)
        embed.add_field(name="Name", value=user.name)
        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Status", value=user.status)
        embed.add_field(name="Highest Role", value=user.top_role)
        embed.add_field(name="Joined this server at", value=str(user.joined_at)[:19])
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        if ctx.channel.permissions_for(ctx.author).create_instant_invite:
            invite_link = "https://discord.com/api/oauth2/authorize?client_id=953037549390151690&permissions=8&scope=bot"
            embed=discord.Embed(title="Invite Jupiter to your own server!", url="https://discord.com/api/oauth2/authorize?client_id=953037549390151690&permissions=8&scope=bot", color=0x00ff99)
            embed.set_author(name="JupiterBot", icon_url="https://scientias.nl/wp-content/uploads/2022/07/jupiter-ringen.jpg")
            embed.set_thumbnail(url="https://scientias.nl/wp-content/uploads/2022/07/jupiter-ringen.jpg")
            embed.add_field(name="Invite Link", value=invite_link)
            await ctx.send(embed=embed)
        else:
            await ctx.send("You don't have enough permission to create invite.")

    @commands.command()
    async def serverinvite(self, ctx):
        if ctx.channel.permissions_for(ctx.author).create_instant_invite:
            invite_link = "https://discord.gg/BNdG4EwYMS"
            embed=discord.Embed(title="Join the official Jupiter Server!", url="https://discord.gg/BNdG4EwYMS", color=0x00ff99)
            embed.set_author(name="JupiterBot", icon_url="https://scientias.nl/wp-content/uploads/2022/07/jupiter-ringen.jpg")
            embed.set_thumbnail(url="https://scientias.nl/wp-content/uploads/2022/07/jupiter-ringen.jpg")
            embed.add_field(name="Invite Link", value=invite_link)
            await ctx.send(embed=embed)
        else:
            await ctx.send("You don't have enough permission to create invite.")




        embed.add_field(name="Joined At", value=user.joined_at)
        await ctx.send(embed=embed)


async def setup(bot):
  await bot.add_cog(ServerInfo(bot))