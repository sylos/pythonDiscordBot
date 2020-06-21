from discord.ext import commands



class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, a, b):
        if (not self.isFloat(a) or not self.isFloat(b)):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(float(a)+ float(b))

    @commands.command()
    async def subtract(self, ctx, a, b):
        if (not self.isFloat(a) or not self.isFloat(b)):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(float(a)-float(b))
    
    @commands.command()
    async def multiply(self, ctx, a, b):
        if (not self.isFloat(a) or not self.isFloat(b)):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(float(a)*float(b))

    @commands.command()
    async def divide(self, ctx, a, b):
        if (not self.isFloat(a) or not self.isFloat(b)):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(float(a)/float(b))

    def isFloat(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

def setup(bot):
    print("Loading Math Cog")
    bot.add_cog(MathCog(bot))

