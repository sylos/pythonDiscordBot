from discord.ext import commands
import random

class Number_game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.number = 0
        self.active_number_game = False
    
    @commands.command(name="start_numbers")
    async def start_game(self, ctx):
        self.number = random.randint(0, 100)
        self.active_number_game = True
        await ctx.send("Player {} has started a number game.".format(ctx.message.author.name))
    
    @commands.command("number_score")
    async def game_status(self, ctx):
        await ctx.send("Game is active: {}".format('Yes' if self.active_number_game else 'No'))

    @commands.command("end_numbers")
    async def stop_game(self, ctx):
        self.active_number_game = False
        await ctx.send("Player {} has ended the game.".format(ctx.message.author.name))
    
    @commands.command("guess")
    async def numbers_game(self, ctx, a):
        if(not self.active_number_game):
            message = "There is no active game at the moment.  Type {}start_numbers to start a new numbers game!".format(self.bot.command_prefix)
            await ctx.send(message)
            return

        if(not a.isnumeric()):
            await ctx.send("Player {} is dumb for sending a string to a numbers game.".format(ctx.message.author.name))
            return

        guess = float(a)
        if(not guess.is_integer()):
            await ctx.send("We only use cardinal numbers here")
            return

        guess = int(a)
        if(guess == self.number):
            self.active_number_game = False
            await ctx.send("{} guessed {} as the correct value!".format(ctx.message.author.name, self.number))
            return
        elif(guess > self.number):
            await ctx.send("{} guess is  high".format(ctx.message.author.name))
        else:
            await ctx.send("{} guess is low".format(ctx.message.author.name))

        await ctx.send("WRONG")

    @commands.command("number")
    async def number_value(self, ctx):
            await ctx.send("Number value is: {}".format(self.number))

def setup(bot):
    print('Loading number game')
    bot.add_cog(Number_game(bot))
