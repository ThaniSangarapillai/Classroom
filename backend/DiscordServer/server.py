# bot.py
import os
import re
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time
import random
import requests
import datetime
import ast

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix="!")

@bot.command(name='addgreeting')
async def addgreeting(ctx, arg, arg_two, arg_three):
    ctx.send("Rans is the big dumb!")

@bot.command(name='mute')
async def addgreeting(ctx):
    for x in bot.get_all_members():
        if x in ctx.message.author.voice.channel.members:
            if x == ctx.message.author:
                continue
            await x.edit(mute=True)
    await ctx.send("Rans is the big dumb!")

@bot.command(name='unmute')
async def addgreeting(ctx):
    for x in bot.get_all_members():
        if x in ctx.message.author.voice.channel.members:
            await x.edit(mute=False)
    await ctx.send("Rans is the big dumb!")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.event
async def on_ready():

    print('{client.user} has connected to Discord!')

def findWholeWord(w, input_str):
    return re.match(r'\b({0})\b'.format(w), input_str)
    #pattern = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search



bot.run(TOKEN)
