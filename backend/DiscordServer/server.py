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
import asyncio
import time
import datetime
import json
#from ..teachingassistant.WebApp import models

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

password = "X7Mz&&am:&dOhnhk|Oq0$W^MYgkD3V|jgp/1*7{5=I4QLC:HFpC&P+FgL>A*w-F"
user = "TeachingAssistant"
classroom_obj = None

bot = commands.Bot(command_prefix="!")

# state
attendance_flag = False
attendance_heres = []

reminders = []

@bot.command(name="initialize")
async def initialize(ctx, *arg):
    try:
        if arg[0] == None:
            await ctx.send("Please enter the email address associated with your account to link your account.")
        elif not re.match("^[a-zA-Z0-9]+@[a-zA-Z]+.[a-z]+$", arg[0]):
            await ctx.send("Please enter the email address associated with your account to link your account.")
        else:
            url = 'http://127.0.0.1:8000/verify/'
            myobj = [{'discord_name': 'Thani4847'}]
            headers = {'content-type': 'application/json'}
            x = requests.post(url, json={"discord_name": str(ctx.message.author), "email": arg[0]}, auth=(user, password), headers=headers)
            classroom_obj = x.json()[0]
            print(classroom_obj)
    except:
        await ctx.send("Please enter the email address associated with your account to link your account.")

@bot.command(name='mute')
async def mute(ctx):
    for x in bot.get_all_members():
        if x in ctx.message.author.voice.channel.members:
            if x == ctx.message.author:
                continue
            await x.edit(mute=True)
    await ctx.send("Rans is the big dumb!")

@bot.command(name='unmute')
async def unmute(ctx):
    for x in bot.get_all_members():
        if x in ctx.message.author.voice.channel.members:
            await x.edit(mute=False)
    await ctx.send("Rans is the big dumb!")

@bot.command(name='list')
async def list(ctx):
    text = "The number of students that are online right now are: 0. Ideally the output would be sorted in this priority: online/not online, alphabetical order."
    await ctx.send(text)

async def take_attendance(ctx, requested_time, requested_endtime):
    await asyncio.sleep(requested_time)

    if requested_endtime == attendance_endtime:
        await ctx.send("Attendance taking is now OVER.\nUsers attending: " + str(len(attendance_heres)))
        global attendance_flag
        attendance_flag = False

@bot.command(name='attendance')
async def attendance(ctx, *args):
    if len(args) == 0:
        requested_time = 60
    else:
        try:
            requested_time = int(args[0])
        except:
            await ctx.send("Usage:\n!attendance x\nwhere x is an integer in seconds.")
            return

    await ctx.send("Taking attendance for " + str(requested_time) + " seconds. Type \"here\" everyone!")
    global attendance_flag, attendance_heres, attendance_endtime
    attendance_flag = True
    attendance_endtime = requested_time + time.time()
    attendance_heres = []

    bot.loop.create_task(take_attendance(ctx, requested_time, attendance_endtime))

@bot.command(name='reminder')
async def reminder(ctx, *args):
    try:
        time = datetime.datetime.strptime(args[0] + " " + args[1], "%d/%m/%Y %H:%M:%S")
        print(time)
        print(type(time))

        await ctx.send(str(time))
    except:
        usage_text = "Usage:\nreminder dd/mm/yyyy xx:yy \"message\""
        await ctx.send(usage_text)
        return



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if attendance_flag and message.content.lower() == "here":
        global attendance_heres
        if message.author not in attendance_heres:
            attendance_heres += [message.author]
        else:
            await message.channel.send("Duplicate user.")

    try:
        await bot.process_commands(message)
    except:
        await message.channel.send("Improper use of command!")

@bot.event
async def on_ready():

    print('{client.user} has connected to Discord!')

def findWholeWord(w, input_str):
    return re.match(r'\b({0})\b'.format(w), input_str)
    #pattern = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


bot.run(TOKEN)

