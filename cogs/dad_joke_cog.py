from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from discord.ext import commands
import random
import json
import aiohttp


DAD_JOKE = 'https://icanhazdadjoke.com/'
class DadJokeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dadjoke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(DAD_JOKE,headers = {'Accept': 'application/json'}) as response:
                if response.status != 200:
                    await ctx.send("Error: Father Not Found")
                data = await response.json()
                joke = (data['joke'])
                await ctx.send(joke)

def setup(bot):
    print("Loading Dad Joke Cog")
    bot.add_cog(DadJokeCog(bot))
