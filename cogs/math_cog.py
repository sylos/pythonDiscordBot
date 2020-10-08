from discord.ext import commands
import operator

#a simple calculator for when the user is too lazy
#to load up one of the million other ones.
#I eventually want to connect it to wolfram alpha
#for more complex systems

#operator commands. addition, multi, etc.  This way
#alleviated some problems with executing user commands
#I did not want to run an 'eval' or such.
ops = {"+": (lambda x,y:x+y),
        "-": (lambda x, y: x-y),
        "*": (lambda x,y: x*y),
        "/": (lambda x,y: x/y)
        }



class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #This command and the following few are old code.  
    #I was exploring a few choices and a literally 'add/subtract' etc 
    #hard coded command was written.  Left in as vestigial code
    #for future refactoring purposes.  
    @commands.command()
    async def add(self, ctx, a, b):
        if (not self.isFloat(a) or not self.isFloat(b)):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(float(a)+ float(b))

    #SEE ADD
    @commands.command()
    async def subtract(self, ctx, a, b):
        if (not self.isFloat(a) or not self.isFloat(b)):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(float(a)-float(b))
    
    #see add
    @commands.command()
    async def multiply(self, ctx, a, b):
        if (not self.isFloat(a) or not self.isFloat(b)):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(float(a)*float(b))

    #see add
    @commands.command()
    async def divide(self, ctx, a, b):
        if (not self.isFloat(a) or not self.isFloat(b)):
            await ctx.send("Please sir, I am only a simple calculator")
            return
        await ctx.send(float(a)/float(b))
    

    #a reworked math system.  Lots of room for expansion, of course,
    #but it's for the future.
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

    #detectss if a number is a floating number or not.  
    def isFloat(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

def setup(bot):
    print("Loading Math Cog")
    bot.add_cog(MathCog(bot))

