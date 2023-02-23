import discord
import random
from discord.ext import commands

class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', aliases=['eight_ball', 'eightball', '8-ball'])
    async def eight_ball(self, ctx, *, question: str):
        """.8ball - Ask the Magic 8-Ball."""
        icon_url = 'https://i.imgur.com/XhNqADi.png'
        responses = [
            'Probably',
            'Without a doubt.',
            'Definitely',
            'You may rely on it.',
            'Most likely.',
            'Use your braincells to think of an answer yourself',
            'Yes.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Do not count on it.',
            'Definitely not',
            'Nah',
            'Very doubtful.',
            'I am too lazy to predict now',
            'I am sorry, I cannot answer that question. My crystal ball is currently being used as a makeshift disco ball at a party in the spirit realm.',
            'According to my calculations, the probability of that happening is approximately 3%. But if you give me a cookie, I will round it up to 50%.',
            'It is possible. But it is also possible that unicorns are real and I am secretly a mermaid. So, you know, take it with a grain of salt',
            'I am sorry, I cannot answer that question. My magic 8ball license has been revoked because I kept giving sarcastic responses',
            'I am getting a strong feeling that the answer is "no" but if you give me a dollar I will say "yes" instead.',
            'I am going to need a little more information before I can give you an accurate prediction. Like your social security number and bank account details',
          'Stop asking me questions. you are annoying',
          'Even I do not know the answer',
          'How about NO?',
          'You wish',
          'Who cares',
          'Fuck you, go away. Why do you think i have the answers you are looking for? Die in a fire.',
          '100%'
        ]
        fortune = random.choice(responses)
        embed = discord.Embed(colour=discord.Colour.purple())
        embed.set_author(name='Magic 8-Ball', icon_url=icon_url)
        embed.add_field(name=f'*{ctx.author.name}, the magic eightball says...*', value=f'**{fortune}**')
        await ctx.send(embed=embed)
        

async def setup(bot):
    await bot.add_cog(EightBall(bot))
