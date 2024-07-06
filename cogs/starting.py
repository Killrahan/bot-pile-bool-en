import discord
from discord.ext import commands 
import csv 

""" 
file dealing with:
-Starting of the bot.
-Bot arriving on a server.
-Member arriving on a server on which the bot is present. 
""" 
class starting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")
        print("------------------------")

    @commands.Cog.listener()
    async def on_guild_join(self,guild): 
        isInFile = False 
        serverID = guild.id 
        
        mydictServer = [{'serverID': f"{serverID}", "nbPile": "0", "prevPlay" : "0"}]
        serverFields = ["serverID", "nbPile", "prevPlay"]
        serverFile = "serverData.csv"
        
        with open(serverFile, "r") as csvfile:
            reader = csv.reader(csvfile)
            for lines in reader:
                if(f"{serverID}" in lines):
                    print("Server already in the file")
                    isInFile = True 
                    break 
                
        if(not isInFile):
            with open(serverFile, "a") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=serverFields)
                writer.writerows(mydictServer)
            
async def setup(bot):
    await bot.add_cog(starting(bot))