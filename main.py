import discord
from discord.ext import commands
from apikeys import *  
from ListDataBank import *  
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",
                   description="bot pile booléen", intents=intents)


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot: 
        await load()
        await bot.start(token)
        
asyncio.run(main())
