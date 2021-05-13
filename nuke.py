import re
import time

import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot, ArgumentParsingError
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
bot = Bot(command_prefix=",", intents=intents)

@bot.command(name="nuke", help="nukes n chats (nukes all chats by default)")
async def nuke(ctx, n=10000):
	print("nuking chats")
	channel = ctx.channel
	await channel.purge(limit=n)
		
@bot.event
async def on_ready():
	print(f"{bot.user} has connected to Discord!")

bot.run(TOKEN)
	
