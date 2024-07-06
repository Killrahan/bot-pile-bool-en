import discord
from discord.ext import commands
from ListDataBank import *
import pandas as pd 
import csv

"""
File related to the game.  
Some informations :
- Score for a specific user is shared among all the server on which the user
  and the bot are presents. (score shared on all servers).
"""

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        game = False 
        
        channelID = message.channel.id 
        channelName = self.bot.get_channel(channelID)
        
        for i in gameList: 
            if (message.content.lower() == i):
                game = True
                break

        
        if(game):
            serverID = message.guild.id
            userID = message.author.id
            
            isInFile = False 
            
            dfUser = pd.read_csv("userData.csv")
            check = dfUser[dfUser['userID'] == userID]
            if(not len(check)):
                dfUser.loc[-1] = [userID,0]
                dfUser.to_csv("userData.csv", index = False)
            
            df = pd.read_csv("serverData.csv")
            index = df.index[df["serverID"] == serverID]
            rightLine = index.astype(int)[0]
        
            rightChan = False

            for i in pChannelName:
                if (i == str(channelName).lower()):
                    rightChan = True
                    break

            if (rightChan == False):
                await message.channel.send("You can't play the game in this channel moron.")
                return
            
            df = pd.read_csv("serverData.csv")
            if(df.loc[rightLine,"prevPlay"] == message.author.id):
                await message.channel.send("You already played dumbass, wait for your turn.")
                return
            
            if (message.content.lower() == "pile"):

                df.loc[rightLine,"nbPile"] += 1
                df.loc[rightLine, "prevPlay"] = message.author.id 
                    
                df.to_csv("serverData.csv", index = False)

                await message.add_reaction("🔋")
                    
            elif((message.content.lower() == "booléen" or message.content.lower() == "booleen") and df.loc[rightLine,"nbPile"] != 0):
                dfUser = pd.read_csv("userData.csv") #df -> server data base, dfUser -> user data base.
                await message.add_reaction("🔟")
        
                author = message.author.id
                username = self.bot.get_user(author)
                nbPile = df.loc[rightLine, "nbPile"]
                scoreGain = int(nbPile*1.6 + 1)
                
                index = dfUser.index[dfUser["userID"] == author]

                dfUser.loc[index,"score"] += scoreGain
                await message.channel.send(f"Game over ! The game lasted for {nbPile} pile, {username.mention} fucked you all and won {scoreGain} points.")
                
                df.loc[rightLine,"prevPlay"] = 0
                df.loc[rightLine,"nbPile"] = 0
                df.to_csv("serverData.csv", index = False)
                
            elif(message.content.lower() == "booléen" or message.content.lower() == "booleen" and df.loc[rightLine,"nbPile"] == 0):
                await message.channel.send("You dumb shit, a game should start with pile try again you looser.")
        
        
async def setup(bot):
    await bot.add_cog(Game(bot))
