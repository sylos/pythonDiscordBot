#!/srv/development/discordBot/pyBot/bin/python

import discord
import random
import sys
import os
import simple_commands
import bot_cogs.number_game
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description='Waddup')
BOT_TOKEN = 'NDY2NDIyOTg5NTI1ODc2NzM2.DjAu1w.3393qog5bqEQs-o8QiTVNpJXHrc'
BOT_OWNER_ID = 118907310243315712


@bot.event
async def on_ready():
    print('logged in as: {}'.format(bot.user.name))
    print('bot ID: {}'.format(bot.user.id))
    print('----')

@bot.command()
async def greet(ctx):
    user =  await bot.fetch_user(ctx.message.author.id)
    await ctx.send(":smiley: :wave: Welcome! {}".format(user.name))

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



@bot.command()
async def add(ctx, a, b):
    if(not a.isnumeric() or not b.isnumeric()):
        await ctx.send("Please sir, I am only a simply calculator.  I can only add numeric digits")
        return
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a:int, b: int):
    await ctx.send(a*b)

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

def main():
    bot.load_extension('simple_commands')
    bot.load_extension('bot_cogs.number_game')
    bot.run(BOT_TOKEN)


if __name__=='__main__':
    main()
