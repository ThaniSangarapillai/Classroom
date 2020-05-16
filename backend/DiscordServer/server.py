# bot.py
import os
import re
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time
import praw
import random
import requests
import datetime
import ast

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

author_message_list = {"Thrushcoil": [True, "pundai.png", None],
                       "Ninjakiller": [False, "Why do we allow people with foot fetishes in here?", None],
                       "slythien": [False, "Go play with your crayons you filthy titan.", None],
                       "Thani": [False, "Greetings Leader <:ltte:691759395784359937>", None],
                       "KingClassic": [False, "Stop falling off of chairs heathen.", None],
                       "TheRunningMan": [False, "Greetings, fellow civil engineer. :tools:", None],
                       "Cashaman": [False, "Greetings, fellow Tamil.", None],
                       "MrMineHeads":[False, "Rajat > Hassan?", None],
}

bot = commands.Bot(command_prefix="!")

reddit = praw.Reddit(client_id='2c4KPAw7ohMDQw',
                     client_secret='4YU5ZGFcOZrcWEOJgb4osGEugrw',
                     user_agent='Thani20')

@bot.command(name='memes')
async def meme(ctx, arg):
    print(arg)
    memes_submissions = reddit.subreddit(arg).hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    await ctx.send(submission.url)

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
    await uniquejoke(message)
    await lanajoke(message)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    global kura_cd, thrush_cd, kevin_cd
    global author_message_list
    try:
        with open("messages.txt", "r") as readfile:
            author_message_list = ast.literal_eval(readfile.read())
    except:
        pass

    for x in author_message_list:
        author_message_list[x][2] = time.time() - 300
    # kura_cd = time.time() - 600
    # thrush_cd = time.time() - 600
    # kevin_cd = time.time() - 600
    print('{client.user} has connected to Discord!')

def findWholeWord(w, input_str):
    return re.match(r'\b({0})\b'.format(w), input_str)
    #pattern = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

async def lanajoke(message):
    #global kevin_cd, thrush_cd, kura_cd
    if message.author != bot.user:
        word = message.content

        if re.match(r'[lL]+[aA4]+[nN]+[aA4]+', word) and str(message.channel) != "bobs":
            await message.channel.send("del rey!")
            time.sleep(5)
        elif (findWholeWord("i'm", word.lower()) or findWholeWord("im", word.lower())) and str(message.channel) != "bobs":
            response = word.split(" ")
            del response[0]
            response = " ".join(response)
            await message.channel.send("Hi {}, I'm Lana!".format(response))
            time.sleep(5)
        elif (findWholeWord("sma", word.lower()) or findWholeWord("smd", word.lower())) and str(message.channel) != "bobs":
            await message.channel.send("Only if you repay the favour :weary:")
            time.sleep(5)
        elif (findWholeWord("owo".lower(), word.lower()) or findWholeWord("uwu".lower(),word.lower())) and str(message.channel) != "bobs":
            await message.channel.send("**O**w**O** what's this?")
            time.sleep(5)

async def uniquejoke(message):
    global author_message_list

    for x in author_message_list.keys():
        if x in str(message.author):
            if time.time() > author_message_list[x][2] + 600:
                if author_message_list[x][0]:
                    await message.channel.send(file=discord.File(author_message_list[x][1]))
                else:
                    await message.channel.send(author_message_list[x][1])
                author_message_list[x][2] = time.time()



bot.run(TOKEN)
