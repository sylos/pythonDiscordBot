from discord.ext import commands


class Simple_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_number_game = False

    
    @commands.command()
    async def chanUsers(self, ctx):
        await ctx.send("Channel Users: {}".format(ctx.channel.members.name))

    @commands.command()
    async def repeat(self,ctx,*, a: str="No strings on me"):
        await ctx.send("You said: {}".format(a))

    @commands.command(name="numbers")
    async def guess_number(self, ctx):
        number = 0
        await ctx.send("Game is active: {}".format(self.active_number_game))
        if (self.active_number_game):
            self.active_number_game = not self.active_number_game
            await ctx.send("We have an active game")
        else:   
            await ctx.send("We shall play Guess the Number!")
            self.active_number_game = not self.active_number_game
            await ctx.send("Number is: {}".format(number))
       
        await ctx.send("Game is active: {}".format(self.active_number_game))
    
    @commands.command(name="quote")
    async def quote_user(self, ctx, *, a: str="No Strings On Me"):
        await ctx.send("You said: {}".format(a))
def setup(bot):
  #     print('Loading test')
    bot.add_cog(Simple_commands(bot))
      #  bot.add_command(chanUsers)
      #  bot.add_command(repeat)


