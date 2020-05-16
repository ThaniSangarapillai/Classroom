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
    global author_message_list
    if "Thani" in str(ctx.message.author.name) or "TheRunningMan" in str(ctx.message.author.name):
        if arg_two == True:
            filename = arg_three.split('/')[-1]
            r = requests.get(arg_three, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            author_message_list[arg] = [arg_two, filename, time.time() - 450]
        else:
            author_message_list[arg] = [arg_two, arg_three, time.time() - 450]

        with open("messages.txt", "w") as writefile:
            writefile.write(str(author_message_list))

        await ctx.send("Updated!")
    else:
        ctx.send("You don't have privs :^)")

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
