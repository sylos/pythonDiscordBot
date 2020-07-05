from discord.ext import commands
import datetime
import random

class Simple_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_number_game = False

   
    @commands.command()
    async def greet(self, ctx):
        mentions = ctx.message.mentions
        greet_people = []

        for x in mentions:
            greet_people.append(x.name)

        if len(greet_people) == 0:
            greet_people.append("Outis")

        await ctx.send(f":smiley: :wave: Hello! {', '.join(greet_people)}")

    @commands.command()
    async def chanUsers(self, ctx):
        await ctx.send("Channel Users: {}".format(ctx.channel.members.name))

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("Meow! =^.^=")

    @commands.command()
    async def repeat(self,ctx,*, a: str="No strings on me"):
        await ctx.send("You said: {}".format(a))
    
    @commands.command(name="utc")
    async def current_time_utc(self, ctx):
        ts = datetime.datetime.now()
        await ctx.send("Current time UTC: {}".format(ts))
    
    @commands.command()
    async def roll(self, ctx, a:str):
        num_dice = float(a.split('d')[0])
        dice_type = float(a.split('d')[1])
        random_value = 0

        for x in(range(int(num_dice))):
            random_value += random.randint(1, int(dice_type))

        await ctx.send("You rolled: {}".format(random_value))
    
    @commands.command(name="quote")
    async def quote_user(self, ctx, *, a: str="No Strings On Me"):
        await ctx.send("You said: {}".format(a))


def setup(bot):
    print("Loading Simple Commands")
    bot.add_cog(Simple_commands(bot))


