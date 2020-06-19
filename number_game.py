from discord.ext import commands


class Number_game(commands.Cog)
    def __init__(self, bot):
        self.bot = bot
        self.active_number_game = False

    async def start_game(self, ctx):
        number = 0
        await ctx.send("Player {} has started a number game." format(ctx.message.author.name))


def setup(bot):
    print('Loading number game')
    bot.add_cog(Number_game(bot))
