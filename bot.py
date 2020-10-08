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
import credentials as cred

#This file handles the core bot loop.  It's all asynchronous
#So that requires designing with asynch processes in mind


#configure the chat command prefix, access the discord bot token
#connect to the DB
bot = commands.Bot(command_prefix='$', description='Waddup')
BOT_TOKEN = cred.BOT_TOKEN
BOT_OWNER_ID = cred.BOT_MASTER_ID
db = DBManagement()

#list of cogs the database has.  A cog is a sort of feature collection
#It handles idealogical chunks of commands.
DEFAULT_COGS = {'simple':'simple_commands'
        ,'math':'cogs.math_cog', 'dadjoke':'cogs.dad_joke_cog'
        ,'numbers':'cogs.number_game'}


#check for certain things when the bot starts up
#on ready is a trigger that the discord.py library sets when
#the bot is confirmed connected and ready for use
@bot.event
async def on_ready():
    print('logged in as: {}'.format(bot.user.name))
    print('bot ID: {}'.format(bot.user.id))
    print('----')
    #grabs the last channel that a shutdown command was given in 
    #and posts a message indicating the bot has restarted.
    #If None was found, sends to a default channel, which is 
    #an admin channel I have.
    shutdown = db.query_latest_shutdown()
    if shutdown != None:
        channel = bot.get_channel(shutdown.channel_id)
        await channel.send("I HAVE AWOKEN!")


#on command runs whenever the discord.py library detects a message
#for the bot to process.  It runs *before* the command is run
#I use it to record a copy of every message the bot runs. 
#I use it for identifying how common a message is used and if there are
#common spelling errors I should account for
@bot.event
async def on_command(ctx):
    db.add_db_command_record(ctx.message)


#triggers when a bot joins a discord server(called guilds).  
#currently copies a list of the users to the database.
@bot.event
async def on_guild_join(guild):
    db.join_guild(guild)

#command that can be run to add users to the DB after the bot
#has already joined the server.  This feature is mostly for bug testing
@bot.command()
async def add_guild_members(ctx):
    db.add_guild_users(ctx.guild)

#fakes the join event, for testing purposes
@bot.command()
async def add_guild(ctx):
    db.join_guild(ctx.guild)

#let's a user pretend to speak as the bot in another channel
#on the same server.  Command is $speak channel #$% message
#where channel is the channel's unique ID, the '#$%' is a not likely 
#key to split the strings
@bot.command()
async def speak(ctx, *, a):
    complete = a.split('#$%')
    if not (len(complete) > 1):
        await ctx.send("You missed the separator")
        return

    channels = ctx.message.channel_mentions
    
    for channel in channels:
        await channel.send(complete[1])
    
    return


#shutdown command.  Checks to see if it's me(the bot owner), otherwise
#denies the user the shutdown command and logs it. Cleans up 
#DB connection and sends a goodbye message to the channel used.
@bot.command()
async def shutdown(ctx):
    if ctx.message.author.id == BOT_OWNER_ID:   
        await ctx.send("Shutting down!")
        db.add_shutdown_command(ctx.message, False)
        db.shutdown()
        sys.exit('Killing Bot')
#log this    
    await ctx.send("""Shutting Down!  Haha...just kidding.  
            {} {} is not authorized""".format(ctx.message.author.name,ctx.message.author.id))

#restart command, similar to shutdown, but automatically restarts the bot
#instead of a complete shutdown
@bot.command()
async def restart(ctx):
    if ctx.message.author.id == BOT_OWNER_ID:
        await ctx.send("Taking a nap then waking!")
        db.add_shutdown_command(ctx.message, True)
        db.shutdown()
        print("Restarting: {}".format(sys.argv))
        print("Running py venv: {}".format(sys.executable))
        os.execl(sys.executable,sys.executable, *sys.argv)
    await ctx.send("I don't wanna!")

#List of simple commands.  Out dated and needs to be updated.
async def command_help(ctx):
    commands =  """```
    commands: greet, add, multiply, cat, roll
    ```"""
    await ctx.send(commands)

#tests whether the bot is connected to the database.  It likely is,
#but until unit tests are implemented, probably decent enough.
#Should configure to call automatically and report errors.
@bot.command()
async def testDB(ctx):
    db.test_db()   
    await ctx.send('Testing DB')

#lists the cogs the bot has.  Cogs are groups of commands and operations
#that work together.  This is useful for the discord API and discord.py
@bot.command(name='cogs')
async def list_cogs(ctx):
    cogs = "```\n"
    for cog in DEFAULT_COGS:
        cogs += str(cog) 
        cogs += "\n"

    cogs += "```"
    await ctx.send(cogs)


#a command to reload a cog if I've modified it.  This is a hotswap
#of the files so the bot doesn't need to restart.
@bot.command(name='reload_ext')
async def reloadExtension(ctx, a):
    if ctx.message.author.id == BOT_OWNER_ID:
        if a in DEFAULT_COGS:
            bot.reload_extension(DEFAULT_COGS[a])
            await ctx.send("Reloading Cog")
            return
    await ctx.send("Not authorized")
    return

#main initializer of the bot.  Called everytime the bot is staretd.
def main():
    for cog in DEFAULT_COGS:
        bot.load_extension(DEFAULT_COGS[cog])

    bot.run(BOT_TOKEN)


if __name__=='__main__':
    main()
