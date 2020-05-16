# bot.py
import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

target = "10"
swearWords = ['temporary']

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    global swearWords

    print('{client.user} has bopped!')
    parent_location = Path(__file__).absolute().parent
    file_location = parent_location / 'swearWords.txt'
    
    file = open(file_location)
    swearWords = [line.rstrip('\n') for line in file]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(swear in message.content for swear in swearWords):
        channel = bot.get_channel(711089932256542721)
        await channel.send(message.author.name + " (" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "): " + message.content )
        await message.delete()
        response = "Please, do not use vulgar language.\nಠ_ಠ"
        await message.channel.send(response)

    elif message.author.id == int(target):
        response = randomBullyQuoteGen()
        await message.channel.send(response)
    
    await bot.process_commands(message)
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("Sorry, only the teacher can use that command.\n¯\_(ツ)_/¯")

@bot.command(name='test')
async def test(ctx,person):
    response = f"ping pang pong {person}"
    await ctx.send(response)
    
@bot.command(name='bully')
@commands.has_role('Teacher')
async def bully(ctx, person):
    global target

    target = person[3:-1:]
    response = f"{person}, you a bitch."
    await ctx.send(response)

@bot.command(name='filter')
@commands.has_role('Teacher')
async def filter(ctx,paramOne,word):
    if (paramOne.lower() == "add"):
        if (word in swearWords):
            response = "This word is already being filtered."
        else:
            swearWords.append(word)
            response = "This word has now been added to the filter."
    elif (paramOne.lower() == "remove"):
        if (word in swearWords):
            swearWords.remove(word)
            response = "This word has been removed from the filer."
        else:
            response = "This word is not part of the filter."

    await ctx.send(response)
    
def randomBullyQuoteGen():
    bully_quotes = [
        'You are a big loser',
        "This is why the other kids don't like you",
        'Get out of my class, dumbo',
        'are you dumb stupid or dumb huh'
    ]
    response = random.choice(bully_quotes)
    return response

bot.run(TOKEN)