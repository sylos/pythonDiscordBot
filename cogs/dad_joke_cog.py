from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from discord.ext import commands
import random
import json


class DadJokeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dadjoke")
    async def dad_joke(self,ctx):
        headers = {'Accept': 'application/json'}
        response =  get('https://icanhazdadjoke.com/', headers=headers)

        if response.status_code == 200:
            data = response.json()
            joke = (data['joke'])
            await ctx.send(joke)
        else:
            await ctx.send('error')

def setup(bot):
    print("Loading Dad Joke Cog")
    bot.add_cog(DadJokeCog(bot))
