import json
import random
import discord
from discord.ext import commands


class economy(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("beg_responses.json", "r") as f:
            self.beg_responses = json.load(f)
        with open("work_responses.json", "r") as f:
            self.work_responses = json.load(f)

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
########## BAL

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, user: discord.User = None):
        user = user or ctx.author
        await self.open_account(ctx.author)
        users = await self.get_bank_data()

        cash_amt = users[str(user.id)]["cash"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title="")
        em.add_field(name="Cash <a:cas:1068463662228049990>",
                     value="{:,}".format(cash_amt))
        em.add_field(name="Bank Balance <a:creditcard:1068486779109396590>",
                     value="{:,}".format(bank_amt))
        em.set_author(name=f"{user.name}'s  Balance", icon_url=user.avatar)

        await ctx.send(embed=em)
#########beg

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def beg(self, ctx):
        await self.open_account(ctx.author)
        users = await self.get_bank_data()
        user = ctx.author
        earnings = random.randrange(50)
        import json

        with open('beg_responses.json') as f:
            beg_responses = json.load(f)

        response = random.choice(self.beg_responses)
        description = response.format(earnings)

        em = discord.Embed(title="",
                           description=description,
                           color=0x3fab62)
        em.set_author(name=f"{user.name}'s  Begging Results", icon_url=user.avatar)
        await ctx.send(embed=em)

        users[str(user.id)]["cash"] += earnings
        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(int(error.retry_after), 60)
            em = discord.Embed(
                title=f"slowdown bro",
                description=
                f"you can beg again in {minutes} minutes and {seconds} seconds",
                color=0xd2171c)
            await ctx.send(embed=em)
##work

    @commands.command()
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def work(self, ctx):
        await self.open_account(ctx.author)

        users = await self.get_bank_data()

        user = ctx.author

        earnings = random.randrange(50, 250)
        response = random.choice(self.work_responses)
        description = response.format(earnings)

        em = discord.Embed(title="",
                           description=description,
                           color=0x3fab62)
        em.set_author(name=f"{user.name}'s  Working Results", icon_url=user.avatar)
        await ctx.send(embed=em)

        users[str(user.id)]["cash"] += earnings

        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(int(error.retry_after), 60)
            hours, minutes = divmod(minutes, 60)
            em = discord.Embed(
                title=f"Take it easy bruh",
                description=
                f"You can work again in {hours} hours, {minutes} minutes, and {seconds} seconds.",
                color=0xd2171c)
            await ctx.send(embed=em)
###withdraw

    @commands.command(aliases=["wt"])
    async def withdraw(self, ctx, amount=None):
        await self.open_account(ctx.author)

        if amount == None:
            await ctx.send("Please specify the amount.")
            return

        users = await self.get_bank_data()
        user_id = str(ctx.author.id)

        if not amount.isdigit():
            await ctx.send("Invalid amount. please provide a valid number")
            return

        amount = int(amount)

        if amount > users[user_id]["bank"]:
            em = discord.Embed(
                title="Transaction Failed",
                description=f"You don't have that much money in the bank.",
                color=0xff0000)
            await ctx.send(embed=em)
        else:
            users[user_id]["cash"] += amount
            users[user_id]["bank"] -= amount
            em = discord.Embed(
                title="Transaction Successful",
                description=
                f'Withdrew {amount} from bank account. Your new bank balance is {users[user_id]["bank"]:,}',
                color=0x00ff00)
            await ctx.send(embed=em)
            with open("mainbank.json", "w") as f:
                json.dump(users, f)

#####deposit

    @commands.command(aliases=["dp"])
    async def deposit(self, ctx, amount=None):
        await self.open_account(ctx.author)
    
        if amount == None:
            await ctx.send("Please specify the amount.")
            return
    
        users = await self.get_bank_data()
        user_id = str(ctx.author.id)
        user = ctx.author
        cash_amt = users[str(user.id)]["cash"]
    
        if amount == "all":
            amount = cash_amt
        else:
            amount = int(amount)
            if amount > cash_amt:
                em = discord.Embed(title="Deposit failed",
                                   description=f"You don't have that much cash.",
                                   color=0xff0000)
                await ctx.send(embed=em)
                return
            if amount < 0:
                await ctx.send("The amount must be above 0")
                return
    
        users[str(user.id)]["cash"] -= amount
        users[str(user.id)]["bank"] += amount
    
        with open("mainbank.json", "w") as f:
            json.dump(users, f)
    
        em = discord.Embed(
            title="Transaction Successful",
            description=
            f'Deposited {amount} to your bank account. Your new bank balance is {users[user_id]["bank"]:,}',
            color=0x00ff00)
        await ctx.send(embed=em)

###########ROB

    @commands.command()
    async def rob(self, ctx, target: discord.User):
        await self.open_account(ctx.author)
        await self.open_account(target)

        users = await self.get_bank_data()

        user = ctx.author
        target_cash = users[str(target.id)]["cash"]

        if target_cash < 100:
            await ctx.send(f"{target.name} doesn't have enough cash to steal.")
            return

        steal_amount = random.randint(50, target_cash)
        users[str(target.id)]["cash"] -= steal_amount
        users[str(user.id)]["cash"] += steal_amount

        em = discord.Embed(
            title="Robbing Results",
            description=
            f"You successfully robbed {steal_amount} coins from {target.name}!"
        )
        await ctx.send(embed=em)

        with open("mainbank.json", "w") as f:
            json.dump(users, f)
###

    @commands.command()
    @commands.is_owner()
    async def superrob(self, ctx, target: discord.Member, amount: int):
        await self.open_account(ctx.author)
        await self.open_account(target)
    
        users = await self.get_bank_data()
    
        user = ctx.author
        target_cash = users[str(target.id)]["bank"]
    
        if target_cash < 100:
            await ctx.send(f"{target.name} doesn't have enough money to steal.")
            return
    
        if amount > target_cash:
            amount = target_cash
    
        users[str(target.id)]["bank"] -= amount
        users[str(user.id)]["bank"] += amount
    
        em = discord.Embed(
            title="Robbing Results",
            description=
            f"You successfully stole {amount} coins from {target.name}'s bank account!"
        )
        await ctx.send(embed=em)
    
        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    @superrob.error
    async def superrob_error(ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")
          
###pay

    @commands.command()
    async def pay(self, ctx, user: discord.User, amount: int):
        await self.open_account(user)
        await self.open_account(ctx.author)

        users = await self.get_bank_data()
        if amount > users[str(ctx.author.id)]["cash"]:
            await ctx.send("You don't have enough cash to pay that amount.")
            return
        if amount < 0:
            await ctx.send("The amount must be above 0")
            return

        users[str(user.id)]["cash"] += amount
        users[str(ctx.author.id)]["cash"] -= amount
        with open("mainbank.json", "w") as f:
            json.dump(users, f)
        await ctx.send(f"You paid {user.name} {amount:,} coins.")

#######buy

    @commands.command()
    async def buy(self, ctx, item_name: str, amount: int):
        await self.open_account(ctx.author)
        users = await self.get_bank_data()
        user = ctx.author

        with open("Store.json", "r") as f:
            store = json.load(f)

        if item_name in store:
            item_cost = store[item_name]['cost']
            total_cost = item_cost * amount

            if users[str(user.id)]["bank"] >= total_cost:
                users[str(user.id)]["bank"] -= total_cost
                if "items" not in users[str(user.id)]:
                    users[str(user.id)]["items"] = {}
                if item_name not in users[str(user.id)]["items"]:
                    users[str(user.id)]["items"][item_name] = {
                        "quantity": amount
                    }
                else:
                    users[str(
                        user.id)]["items"][item_name]["quantity"] += amount
                em = discord.Embed(
                    title=f"Purchase Successful",
                    description=
                    f"You have bought {amount} {item_name} for {total_cost}")
                await ctx.send(embed=em)
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)
            else:
                em = discord.Embed(
                    title="Transaction Failed",
                    description=
                    "You do not have sufficient funds <a:laugh:1068475227069222932>"
                )
                await ctx.send(embed=em)
        else:
            em = discord.Embed(title="Transaction Failed",
                               description="Item not available in store")
            await ctx.send(embed=em)

#########bag

    @commands.command()
    async def bag(self, ctx, member: discord.Member = None):
        with open("mainbank.json", "r") as f:
            users = json.load(f)
    
        user = member if member else ctx.author
        user_id = str(user.id)
        user_items = users[user_id].get("items", {})
    
        if not user_items:
            em = discord.Embed(
                title=f"{user.name}'s bag is empty",
                description="This user has not bought any items yet.")
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title=f"{user.name}'s bag",
                               description="List of items in this user's bag")
            for item_name, item_data in user_items.items():
                em.add_field(name=item_name,
                             value=f"Quantity: {item_data['quantity']}")
            await ctx.send(embed=em)

#######store

    @commands.command()
    async def shop(self, ctx):
        with open("Store.json", "r") as f:
            store = json.load(f)

        items = [(item_name, item_data["cost"]) for item_name, item_data in store.items()]
        items.sort(key=lambda x: x[1])
    
        em = discord.Embed(title="wanna be off brand wallmart Bot Store",
                           description="List of items available for purchase")
        for item_name, item_cost in items:
            em.add_field(name=item_name,
                         value=f"Cost: {'{:,}'.format(item_cost)}")
        await ctx.send(embed=em)

#####use

    @commands.command()
    async def use(self, ctx, item_name: str):
        with open("mainbank.json", "r") as f:
            users = json.load(f)

        user = ctx.author
        user_items = users[str(user.id)].get("items", {})

        if item_name not in user_items:
            em = discord.Embed(
                title="Item not found",
                description="You do not have this item in your bag.")
            await ctx.send(embed=em)
        else:
            user_items[item_name]["quantity"] -= 1
            if user_items[item_name]["quantity"] == 0:
                del user_items[item_name]
                em = discord.Embed(
                    title=f"You used your last {item_name}",
                    description="You have no more of this item in your bag.")
            else:
                em = discord.Embed(
                    title=f"You used an {item_name}!",
                    description=
                    f"You now have {user_items[item_name]['quantity']}  {item_name}(s) left in your bag!"
                )
            await ctx.send(embed=em)
            users[str(user.id)]["items"] = user_items
            with open("mainbank.json", "w") as f:
                json.dump(users, f)
#######sell

    @commands.command()
    async def sell(self, ctx, item_name: str, amount: int):
        with open("mainbank.json", "r") as f:
            users = json.load(f)

        user = ctx.author
        user_items = users[str(user.id)].get("items", {})

        if item_name not in user_items:
            em = discord.Embed(
                title="Item not found",
                description="You do not have this item in your bag.")
            await ctx.send(embed=em)
        else:
            if user_items[item_name]["quantity"] < amount:
                em = discord.Embed(
                    title="Not Enough",
                    description=
                    f"You only have {user_items[item_name]['quantity']} of this item in your bag."
                )
                await ctx.send(embed=em)
            else:
                with open("Store.json", "r") as f:
                    store = json.load(f)
                item_cost = store[item_name]['cost']
                total_earnings = (item_cost // 2) * amount
                users[str(user.id)]["cash"] += total_earnings
                user_items[item_name]["quantity"] -= amount
                if user_items[item_name]["quantity"] == 0:
                    del user_items[item_name]
                    em = discord.Embed(
                        title=f"Sold {amount} {item_name}",
                        description=
                        f"You earned {total_earnings} coins and have no more of this item in your bag."
                    )
                else:
                    em = discord.Embed(
                        title=f"Sold {amount} {item_name}",
                        description=
                        f"You earned {total_earnings} coins and now have {user_items[item_name]['quantity']} of this item in your bag."
                    )
                await ctx.send(embed=em)
                users[str(user.id)]["items"] = user_items
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)

#####buyrole

    @commands.command()
    async def premium(self, ctx):
        with open("mainbank.json", "r") as f:
            users = json.load(f)
        user = ctx.author
        user_id = str(user.id)
        premium_role = discord.utils.get(ctx.guild.roles, name="Premium-Member")
        if premium_role in user.roles:
            await ctx.send("You already have this role.")
        else:
            if users[user_id]["cash"] < 25000:
                await ctx.send(
                    "You don't have enough cash to buy this role. (you need 25000)"
                )
            else:
                users[user_id]["cash"] -= 25000
                try:
                    await user.add_roles(premium_role)
                    await ctx.send("You have successfully bought the Premium role.")
                except Exception as e:
                    await ctx.send(f"Error adding role: {e}")
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)

####LEADERBOARD

    @commands.command()
    async def leaderboard(self, ctx):
        users = await self.get_bank_data()
        sorted_users = sorted(users.items(),
                              key=lambda x: x[1]["bank"],
                              reverse=True)
        top_5 = sorted_users[:5]

        leaderboard_str = ""
        for i, user in enumerate(top_5):
            leaderboard_str += f"{i+1}. {self.client.get_user(int(user[0])).name} Has {format(user[1]['bank'], ',')} coins in their bank account\n"

        em = discord.Embed(
            title=
            "JupiterBot's top 5 richest users (EVERY server the bot is in. is counted)",
            description=leaderboard_str,
            color=0x3fab62)
        await ctx.send(embed=em)


###########
item = {"iPhone": {"cost": 1200}}

with open("Store.json", "r") as f:
    store = json.load(f)

store.update(item)

with open("Store.json", "w") as f:
    json.dump(store, f)
### DO NOT PUT CODE UNDER THIS


async def setup(bot):
    await bot.add_cog(economy(bot))
