from discord.ext import commands
import operator
ops = {"+": (lambda x,y:x+y),
        "-": (lambda x, y: x-y),
        "*": (lambda x,y: x*y),
        "/": (lambda x,y: x/y)
        }



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
    

    @commands.command()
    async def math(self, ctx, *, a):
        math_expr = a.split(" ")
        #check if operator is legal operator(+-*/)
        if (not math_expr[0] in ops.keys()):
            await ctx.send("Not a legal operator for this bot")
            return
        
        operator = math_expr[0]
        if (not self.isFloat(math_expr[1]) and not self.isFloat(math_expr[2])):
            await ctx.send("Only integers and floats allowed")
            return

        value = (ops[operator](float(math_expr[1]),float(math_expr[2])))

        await ctx.send(value)

    def isFloat(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

def setup(bot):
    print("Loading Math Cog")
    bot.add_cog(MathCog(bot))

