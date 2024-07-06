
import discord
from discord.ext import commands
from ListDataBank import *
import pandas as pd
""" 
Basically deals with all commands.
""" 
class ChannelHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addChannel(self,ctx,arg):
        if (len(pChannelName) <= 20):
            pChannelName.append(arg)
            print("new channel added.")
        else:
            await ctx.send("You added too many channel, bot must be restarted to add more.")

    @commands.command()
    async def helpUse(self,ctx):
        await ctx.send(""" 
        
                  How to make the bot works : 
                
                   1) Create a channel named "pile-ou-boolé(e)en".
                      
                   2) Once the bot is added to a channel, one can start
                      a game by writting "pile" in the channel.
                     
                   """)
    @commands.command()
    async def score(self,ctx):
        df = pd.read_csv("userData.csv")
        userID = ctx.message.author.id 
        print("user id is : ", userID)
        index = df.index[df["userID"] == userID]
        print(index)
        score = df.iloc[index,1]
        print(score.values)
        await ctx.send(f"Your score is {score.values[0]}")
        
async def setup(bot):
    await bot.add_cog(ChannelHandling(bot))



