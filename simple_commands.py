import discord
from discord.ext import commands

@commands.command()
async def test(ctx):
    await ctx.send("this test worked")

