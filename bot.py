#!/srv/development/discordBot/pyBot/bin/python

import discord
import random
import sys
import os
import simple_commands
import cogs.number_game
import cogs.math_cog
from discord.ext import commands
from dbManagement.dbManager import DBManagement

bot = commands.Bot(command_prefix='$', description='Waddup')
BOT_TOKEN = 'NDY2NDIyOTg5NTI1ODc2NzM2.DjAu1w.3393qog5bqEQs-o8QiTVNpJXHrc'
BOT_OWNER_ID = 118907310243315712
db = DBManagement()

@bot.event
async def on_ready():
    print('logged in as: {}'.format(bot.user.name))
    print('bot ID: {}'.format(bot.user.id))
    print('----')

@bot.command()
async def greet(ctx):
    mentions = ctx.message.mentions
    greet_people = []
    for x in mentions:
        greet_people.append(x.name)

    if len(greet_people) == 0:
        greet_people.append("Outis")
    await ctx.send(f":smiley: :wave:  Hello! {', '.join(greet_people)}")

@bot.event
async def on_command(ctx):
    db.add_db_command_record(ctx.message)

@bot.command()
async def shutdown(ctx):
    if ctx.message.author.id == BOT_OWNER_ID:   
        await ctx.send("Killing myself!")
        sys.exit('Killing Bot')
#log this    
    await ctx.send("""Killing myself!  Haha...just kidding.  
            {} {} is not authorized""".format(ctx.message.author.name,ctx.message.author.id))

@bot.command()
async def restart(ctx):
    if ctx.message.author.id == BOT_OWNER_ID:
        await ctx.send("Taking a nap then waking!")
        print("Restarting: {}".format(sys.argv))
        print("Running py venv: {}".format(sys.executable))
        os.execl(sys.executable,sys.executable, *sys.argv)
    #log this with author
    await ctx.send("I don't wanna!")

@bot.command(name='author')
async def authorID(ctx):
    await ctx.send("author is: {}".format(
        ctx.message.author.id))

@bot.command()
async def cat(ctx):
    await ctx.send('Meow! =^.^=')

@bot.command()
async def roll(ctx, a:str):
    num_dice = float(a.split('d')[0])
    dice_type = float(a.split('d')[1])
    random_value = 0

    for x in range(int(num_dice)):
        random_value += random.randint(1, int(dice_type))

    await ctx.send("You rolled: {}".format(random_value))

@bot.command()
async def command_help(ctx):
    commands =  """```
    commands: greet, add, multiply, cat, roll
    ```"""
    await ctx.send(commands)

@bot.command()
async def testDB(ctx):
    db.test_db()   
    await ctx.send('Testing DB')
def main():
    bot.load_extension('simple_commands')
    bot.load_extension('cogs.number_game')
    bot.load_extension('cogs.math_cog')
    bot.load_extension('cogs.dad_joke_cog')
    bot.run(BOT_TOKEN)


if __name__=='__main__':
    main()
