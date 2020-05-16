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

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix="!")

# state
attendance_flag = False
attendance_heres = []

reminders_dict = {}

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

    await bot.process_commands(message)

@bot.event
async def on_ready():

    print('{client.user} has connected to Discord!')

def findWholeWord(w, input_str):
    return re.match(r'\b({0})\b'.format(w), input_str)
    #pattern = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search



bot.run(TOKEN)
