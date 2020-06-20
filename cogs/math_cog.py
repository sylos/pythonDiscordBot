from discord.ext import commands



class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(ctx, a, b):
        if (not a.isnumeric() or not b.isnumeric()):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(a+b)

    @commands.command()
    async def subtract(ctx, a, b):
        if (not a.isnumeric() or not b.isnumeric()):
            await ctx.send("Please sir, I am only a simple calculator")
        await ctx.send(a-b)
    
    @commands.command()
    async def multiply(ctx, a, b):
        if (not a.isnumeric() or not b.isnumeric()):
            await ctx.send("Please sir, I am only a simple calculator")
        await ctx.send(a*b)

    @commands.command()
    async def divide(ctx, a, b):
        if (not a.isnumeric() or not b.isnumeric()):
            await ctx.send("Please sir, I am only a simple calculator")
        await ctx.send(a/b)


def setup(bot):
    print("Loading Math Cog")
    bot.add_cog(MathCog(bot))

