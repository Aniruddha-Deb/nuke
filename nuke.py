import re
import time

import discord
import os
from datetime import datetime
import time
from discord.ext import commands
from discord.ext.commands import Bot, ArgumentParsingError
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
bot = Bot(command_prefix=",", intents=intents)

def utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

@bot.command(name="nuke", help="nukes n chats (nukes all chats by default)")
async def nuke(ctx, n=10000):
	print("nuking chats")
	channel = ctx.channel
	await channel.purge(limit=n)

@bot.command(name="archive", help="archives n chats (archives all chats by default)")
async def archive(ctx, n=10000):
	print("Archiving chats")
	outfile = open("output/archive.txt", "w")
	channel = ctx.channel
	messages = await channel.history(limit=n).flatten()
	for message in reversed(messages):
		time = utc_to_local(message.created_at).strftime("%d/%m/%y %I:%M:%S %p")
		outfile.write(f"[{time}] {message.author.name}: {message.content}\n")
	
	outfile.close()
	await ctx.send(file=discord.File('output/archive.txt'))
		
@bot.event
async def on_ready():
	print(f"{bot.user} has connected to Discord!")

bot.run(TOKEN)
	
