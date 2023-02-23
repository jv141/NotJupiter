import json
import random
import discord
from discord.ext import commands
from discord import Color

class gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    async def update_bank(self, user, amount):
      users = await self.get_bank_data()
      if str(user.id) in users:
          users[str(user.id)]["bank"] += amount
          with open("mainbank.json", "w") as f:
              json.dump(users, f)


    @commands.command()
    async def lottery(self, ctx):
        cost = 1000
        winnings = 50000
        win_chance = 0.05
        await self.open_account(ctx.author)
        users = await self.get_bank_data()
        user_id = str(ctx.author.id)
        
        if users[user_id]["cash"] < cost:
            await ctx.send("You do not have enough cash to enter the lottery. (you need 1000)")
            return

        users[user_id]["cash"] -= cost
        with open("mainbank.json", "w") as f:
            json.dump(users, f)

        win = random.random() < win_chance
        if win:
            users[user_id]["cash"] += winnings
            with open("mainbank.json", "w") as f:
                json.dump(users, f)
            result = f"Congratulations! You won {winnings} coins in the lottery!"
        else:
            result = "Sorry, you lost. Better luck next time LOSER <a:laugh:1068475227069222932> <:palpi:1070785387733188690> <:skeletor:1070785436286451872>"

        em = discord.Embed(title="Lottery Results", description=result, color=0xd9048e)
        em.set_author(name='The Grand Jupiter Casino')
        await ctx.send(embed=em)


    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def slots(self, ctx, amount=None):
        await self.open_account(ctx.author)
        icon_url = 'https://e7.pngegg.com/pngimages/888/549/png-clipart-double-diamond-fruit-machines-money-wheel-slot-machine-game-classic-slots-free-casino-slot-games-classic-slot-machine-free-others-game-logo.png'
        users = await self.get_bank_data()
        user_id = str(ctx.author.id)

        if amount == None:
            await ctx.send("Please specify the amount.")
            return
        if not amount.isnumeric():
            await ctx.send("Please enter a valid number.")
            return
        if int(amount) <= 0:
            await ctx.send("Please enter an amount greater than 0.")
            return
        if int(amount) > users[user_id]["cash"]:
            await ctx.send("You do not have enough cash to use the slots.")
            return

        users[user_id]["cash"] -= int(amount)

        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    # list of possible emojis
        emojis = ["🍎", "🍐", "🍊", "🍉"]
    # generate 3 random emojis
        slot_result = [random.choice(emojis) for i in range(3)]
    # check if all 3 emojis are the same
        if all(x == slot_result[0] for x in slot_result):
            color = 0x11e835
            winnings = int(amount) * 2
            result = f"{' '.join(slot_result)} | Y-You cheated and won {winnings} coins! <:flush:1068471524245385247>"
            users[user_id]["cash"] += winnings
            with open("mainbank.json", "w") as f:
                json.dump(users, f)
        else:
            result = f"{' '.join(slot_result)} | You lost... LOSER <a:laugh:1068475227069222932> <:palpi:1070785387733188690>"
            color = 0xc51b1b
        em = discord.Embed(title="Slot Machine Results", description=result, color=color)
        em.add_field(name="", value="Thank you for p(l)aying", inline=False)
        em.set_author(name='The Grand Jupiter Casino', icon_url=icon_url)
        await ctx.send(embed=em)

    @slots.error
    async def slots_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"take it easy bruh",description=f"you can use the slots again in {error.retry_after:.2f} seconds",color=0xd2171c)
            await ctx.send(embed=em)


    @commands.command(name='blackjack', aliases=['bj', 'jackblack'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def blackjack(self, ctx, bet=None):
        icon_url = 'https://t4.ftcdn.net/jpg/03/39/46/17/360_F_339461727_gMYWEkhtsf67tdp7gWjgCqUF3IS1i8EE.jpg'
        await self.open_account(ctx.author)
        users = await self.get_bank_data()
        user_id = str(ctx.author.id)
    
        if bet == None:
            em = discord.Embed(title="Blackjack", description="Please specify the bet amount.")
            em.set_author(name='The Grand Jupiter Casino', icon_url=icon_url)
            await ctx.send(embed=em)
            return
        if not bet.isnumeric():
            em = discord.Embed(title="Blackjack", description="Please enter a valid number.")
            em.set_author(name='The Grand Jupiter Casino', icon_url=icon_url)
            await ctx.send(embed=em)
            return
        if int(bet) <= 0:
            em = discord.Embed(title="Blackjack", description="Please enter a bet amount greater than 0.")
            em.set_author(name='The Grand Jupiter Casino', icon_url=icon_url)
            await ctx.send(embed=em)
            return
        if int(bet) > users[user_id]["cash"]:
            em = discord.Embed(title="Blackjack", description="You do not have enough cash to play blackjack.")
            em.set_author(name='The Grand Jupiter Casino', icon_url=icon_url)
            await ctx.send(embed=em)
            return
            #subtract the bet amount from the user's cash
        
        with open("mainbank.json", "w") as f:
            json.dump(users, f)
    
            # code for the blackjack game
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        dealer_cards = [random.choice(cards) for _ in range(2)]
        player_cards = [random.choice(cards) for _ in range(2)]
        dealer_total = sum(dealer_cards)
        player_total = sum(player_cards)
        result = ""
        while True:
            em = discord.Embed(title="Blackjack", description="")
            em.add_field(name="Your hand:", value="{} (Total: {})\n".format(player_cards, player_total))
            em.add_field(name="Do you want to draw another card?", value="(yes/no)")
            em.set_author(name='The Grand Jupiter Casino', icon_url=icon_url)
            em.color=0xd9048e
            await ctx.send(embed=em)
            response = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)
            if response.content.lower() == "yes":
                new_card = random.choice(cards)
                player_cards.append(new_card)
                player_total += new_card
                if player_total > 21:
                    result = "You lost, You went over 21!"
                    users[user_id]["cash"] -= int(bet)
                    with open("mainbank.json", "w") as f:
                        json.dump(users, f)
                    break
            elif response.content.lower() == "no":
                while dealer_total < 17:
                    new_card = random.choice(cards)
                    dealer_cards.append(new_card)
                    dealer_total = sum(dealer_cards)
                    if dealer_total > 21: # check if dealer goes over 21
                        result =f"You won {int(bet) * 2} coins!, Jupiter went over 21! <:bigbird:1070785487935123476>"
                        users[user_id]["cash"] += int(bet) * 2 # double the bet amount
                        with open("mainbank.json", "w") as f:
                            json.dump(users, f)
                        break
                if dealer_total <= 21:
                    if player_total > dealer_total:
                        result =f"You won , Your hand is higher than Jupiter's! .. You won {int(bet) * 2} coins! :D <:bigbird:1070785487935123476>"
                        users[user_id]["cash"] += int(bet) * 2 # double the bet amount
                        with open("mainbank.json", "w") as f:
                            json.dump(users, f)
                    elif player_total < dealer_total:
                        result = "You lost, Jupiter's hand is higher than yours. <:palpi:1070785387733188690>"
                        users[user_id]["cash"] -= int(bet)
                        with open("mainbank.json", "w") as f:
                            json.dump(users, f)
                    else:
                        result = "It's a tie!"
                break
            else:
                em = discord.Embed(title="Blackjack", description="Please enter a valid response.")
                em.set_author(name='The Grand Jupiter Casino', icon_url=icon_url)
                await ctx.send(embed=em)
        em = discord.Embed(title="Blackjack result", description="Jupiter's hand: {} (Total: {})\nYour hand: {} (Total: {})\n{}".format(dealer_cards, dealer_total, player_cards, player_total, result))
        em.color=0xd9048e
        em.set_author(name='The Grand Jupiter Casino', icon_url=icon_url)
        await ctx.send(embed=em)

    @blackjack.error
    async def blackjack_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"take it easy bruh",description=f"you can play blackjack again in {error.retry_after:.2f} seconds")
            await ctx.send(embed=em)


    @commands.command()
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def race(self, ctx, bet: int, *racers: str):
        await self.open_account(ctx.author)
        users = await self.get_bank_data()
        user_id = str(ctx.author.id)
    
        if bet < 1:
            await ctx.send("You must bet at least 1 cash.")
            return
    
        if users[user_id]["cash"] < bet:
            await ctx.send("You don't have enough cash to make that bet.")
            return
    
        available_racers = ["Trump", "Obama", "Hitler", "Je Moeder", "Gandhi", "Satan", "Jesus", "Shit", "Bin Laden", "A Raccoon", "Stalin", "Putin"]
        racer = ' '.join(racers)
        if racer not in available_racers:
            await ctx.send("Invalid racer: {}.\nPlease choose one of the available racers: {}".format(racer, ", ".join(available_racers)))
            return
    
        users[user_id]["cash"] -= bet
    
        random.shuffle(available_racers)
        results = available_racers[:3]
    
        em = discord.Embed(title="Top Three Racers", color=0x3fab62)
        em.add_field(name="🥇 First Place", value=results[0], inline=False)
        em.add_field(name="🥈 Second Place", value=results[1], inline=False)
        em.add_field(name="🥉 Third Place", value=results[2], inline=False)
        await ctx.send(embed=em)
    
        if racer == results[0]:
            winnings = bet * 5
            message = "{} won!, You won {} cash!".format(racer, winnings)
        else:
            winnings = 0
            message = "Better luck next time!"
    
        users[user_id]["cash"] += winnings
    
        em = discord.Embed(title="Race Results", description=message, color=0x3fab62)
        em.add_field(name="Your Bet", value=bet)
        em.add_field(name="Your Winnings", value=winnings)
        em.add_field(name="Your Total Cash", value=users[user_id]["cash"])
        await ctx.send(embed=em)
    
        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    @race.error
    async def race_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(int(error.retry_after), 60)
            hours, minutes = divmod(minutes, 60)
            em = discord.Embed(
                title=f"Take it easy bruh",
                description=
                f"You can bet on da race again in {hours} hours, {minutes} minutes, and {seconds} seconds.",
                color=0xd2171c)
            await ctx.send(embed=em)

    @commands.command()
    async def racers(self, ctx):
        racers = ["Trump", "Obama", "Hitler", "Je Moeder", "Gandhi", "Satan", "Jesus", "Shit", "Bin Laden", "A Raccoon", "Stalin", "Putin"]
        em = discord.Embed(title="Available Racers", color=0x3fab62)
        for i, racer in enumerate(racers):
            em.add_field(name=f"{racer}", value="\u200b", inline=True)
        await ctx.send(embed=em)


      
async def setup(bot):
    await bot.add_cog(gamble(bot))