from discord.ext import commands
import operator
import credentials as cred
import json

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint

ts = TimeSeries(key=cred.ALPHA_VANTAGE_KEY)
cc = CryptoCurrencies(key=cred.ALPHA_VANTAGE_KEY)
fx = ForeignExchange(key=cred.ALPHA_VANTAGE_KEY)

#stock market data. 
#will be using the alpha vantage stock market once I get my API key

class StockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #will accept a stock and return results based on info from alpha vantage(or perhaps others)
    #time slices will probably be an instant right now instead of a chunk of day
    @commands.command()
    async def stock(self, ctx, stock):
        data,meta_data = ts.get_quote_endpoint(symbol=stock) 

        await ctx.send(self.printData(data))
   
    @commands.command()
    async def crypto(self, ctx, crypto):
        data,meta_data = cc.get_digital_currency_exchange_rate(crypto, 'USD')
           
        await ctx.send(self.printData(data))

    @commands.command()
    async def exchange(self,ctx, cur_from='eur', cur_to='usd'):
        data,_ = fx.get_currency_exchange_rate(cur_from, cur_to)
        print(data)
        await ctx.send(self.printData((data)))

    def printData(self, data):
        message = "```\n"
        for key in data:
            message += key + ": " + data[key] + '\n'

        message += "```"
        return  message


def setup(bot):
    print("Loading Stock Cog")
    bot.add_cog(StockCog(bot))
