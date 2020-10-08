from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from discord.ext import commands
import random


'''
Built off the beautiful soup/requests tutorial. 
Goes to a dadjoke website and scrapes it for a dad joke
This is not a solid method.  Not generic, not sturdy.  A simple
change to the website would render this not working.
It's on my todo list to rework this
'''
class DadJokeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def simple_get_dadjokes(self, url):
        try:
            with closing(get(url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None
        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(url, str(e)))

    def is_good_response(self, resp):
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') >= 0)

    def log_error(e):
        print(e)

    #uses beautiful soup to parse a website for a dad joke
    #and a dad joke pun
    def parse_dadjokes(self, content):
        #need to not magic number this
        joke_value = random.randint(0,6) 
        html = BeautifulSoup(content, 'html.parser')
        all_jokes= html.find_all("div", {"class": "riddle-cont"})
        joke = []
        joke.append(all_jokes[joke_value].contents[1].h1.get_text())
        joke.append(all_jokes[joke_value].contents[3].string.strip())
        return joke

    @commands.command(name="dadjoke")
    async def get_dadjoke(self, ctx):
        #need to not magic number this
        page = random.randint(0, 329)
        print("page index" + str(page))
        content = self.simple_get_dadjokes('https://www.dadjokes.org/?page='+str(page))
        joke = self.parse_dadjokes(content)
        await ctx.send(f'```{joke[0]}\n{joke[1]}```')

def setup(bot):
    print("Loading Dad Joke Cog")
    bot.add_cog(DadJokeCog(bot))
