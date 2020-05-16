# bot.py
import os
import re
import discord
from discord.ext import commands, tasks
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

channel_reminders = 711102253800620073

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
            print("wow!")
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

@bot.command(name="currentreminders")
async def currentreminders(ctx, *args):
    text = ""
    i = 0

    for reminder in reminders:
        (datetime, message) = reminder
        text += str(i) + ":"
        text += " " + str(datetime)
        text += " " + "\"" + message + "\""
        text += "\n"
        i += 1

    await ctx.send(text)

@bot.command(name='reminder')
async def reminder(ctx, *args):
    try:
        time = datetime.datetime.strptime(args[0] + " " + args[1], "%d/%m/%Y %H:%M:%S")
        print(time)

        global reminders
        reminders += [(time, args[2])]
        await ctx.send("A reminder has been added.")
    except:
        usage_text = "Usage:\n!reminder dd/mm/yyyy hh:mm:ss \"message\""
        await ctx.send(usage_text)
        return

@bot.command(name='removereminder')
async def removereminder(ctx, *args):
    try:
        index = int(args[0])
        global reminders
        toremove = reminders[index]
        reminders.pop(index)

        (datetime, message) = toremove
        text = str(index) + ":"
        text += " " + str(datetime)
        text += " " + "\"" + message + "\""
        text += "\n"
        print("REMOVED " + text)
        await ctx.send("removed the following reminder:\n" + text)
    except:
        usage_text = "Usage:\n!removereminder index"
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

@tasks.loop(seconds=1)
async def once_a_second():
    # check reminders
    global reminders
    currentdatetime = datetime.datetime.now()
    remove_reminders = []

    for reminder in reminders:
        (reminderdatetime, message) = reminder

        if reminderdatetime <= currentdatetime:
            print("Reminder! " + message)
            remove_reminders += [reminder]
            channel = bot.get_channel(channel_reminders)
            await channel.send(message)

    reminders = [r for r in reminders if r not in remove_reminders]

    print(reminders)

@once_a_second.before_loop
async def before_once_a_second():
    await bot.wait_until_ready()

once_a_second.start()
bot.run(TOKEN)
