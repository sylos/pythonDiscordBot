from discord.ext import commands
import discord
import datetime
import random
import io
import aiohttp

#A bunch of very simple commands (greet, etc)
#These were the first sets of commands written for the bot
#pretty self explanatory.

cat_url = 'https://aws.random.cat/meow'
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
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(cat_url) as resp:
                if resp.status != 200:
                    return await channel.send('Could not download file...')
                
                image_url = await resp.json()
                async with session.get(image_url['file']) as image:
                    if image.status != 200:
                        return await channel.send('blagh')
    
                    data = io.BytesIO(await image.read())

               
            await ctx.channel.send(file=discord.File(data, 'cat.png'))

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


