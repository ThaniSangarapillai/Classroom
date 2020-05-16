# bot.py
import os
import re
import discord
from discord.ext import commands, tasks
from discord.utils import get
from dotenv import load_dotenv
import time
import random
import requests
import datetime
import ast
import asyncio
import time
import json
from pathlib import Path
# from ..teachingassistant.WebApp import models
from enum import Enum


# all required roles that should be present at all times go here
class Roles(Enum):
    TEACHER = "Teacher"
    TA = "TA"
    STUDENT = "Student"


# all required text channels that should be present at all times go here
class TextChannels(Enum):
    REMINDERS = "reminders"
    TEACHERS_LOUNGE = "teachers-lounge"


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

password = "X7Mz&&am:&dOhnhk|Oq0$W^MYgkD3V|jgp/1*7{5=I4QLC:HFpC&P+FgL>A*w-F"
user = "TeachingAssistant"
classroom_obj = None

bot = commands.Bot(command_prefix="!")

channel_reminders = 711102253800620073
student_roleid = 711143892304527360

# state
attendance_flag = False
attendance_heres = []

reminders = {}

groups = []
email = ""
name = ""
discord_name = ""
swearWords = []


async def getRole(guild, name, colour=0x1fff7c):
    role = get(guild.roles, name=name)
    if role is None:
        return await guild.create_role(name=name, colour=discord.Colour(colour))
    else:
        return role


async def getChannel(guild, name):
    print(name, type(name))
    name = name.lower()
    channel = get(guild.channels, name=name)
    if channel is None:
        return await guild.create_text_channel(name=name)
    else:
        return channel


async def getMembersOfRole(guild, role_name):
    role = await getRole(guild, role_name)

    members = []
    for member in guild.members:
        if role in member.roles:
            members += [member]

    return members


@bot.command(name="setup")
async def setup(ctx, *args):
    guild = ctx.guild
    await getRole(guild, Roles.STUDENT.value, 0x1fff7c)
    await getRole(guild, Roles.TEACHER.value, 0xff4af9)
    await getRole(guild, Roles.TA.value, 0x3bffef)
    await getChannel(guild, TextChannels.REMINDERS.value)
    await getChannel(guild, TextChannels.TEACHERS_LOUNGE.value)

    global discord_name, email, user, password
    # try:
    if args[0] == None:
        await ctx.send("Please enter the email address associated with your account to link your account.")
    elif not re.match("^[a-zA-Z0-9]+@[a-zA-Z]+.[a-z]+$", args[0]):
        await ctx.send("Please enter the email address associated with your account to link your account.")
    else:
        url = 'http://34.125.57.52/verify/'
        myobj = [{'discord_name': 'Thani4847'}]
        headers = {'content-type': 'application/json'}
        x = requests.post(url, json={"discord_name": str(ctx.message.author), "email": args[0]},
                          auth=(user, password), headers=headers)
        classroom_obj = x.json()[0]
        discord_name = str(ctx.message.author)
        email = args[0]
        print(classroom_obj)
        setSwearWordList()


# @bot.command(name="initialize")
# async def initialize(ctx, *arg):
#     global discord_name, email, user, password
#     # try:
#     if arg[0] == None:
#         await ctx.send("Please enter the email address associated with your account to link your account.")
#     elif not re.match("^[a-zA-Z0-9]+@[a-zA-Z]+.[a-z]+$", arg[0]):
#         await ctx.send("Please enter the email address associated with your account to link your account.")
#     else:
#         url = 'http://34.125.57.52/verify/'
#         myobj = [{'discord_name': 'Thani4847'}]
#         headers = {'content-type': 'application/json'}
#         x = requests.post(url, json={"discord_name": str(ctx.message.author), "email": arg[0]},
#                           auth=(user, password), headers=headers)
#         classroom_obj = x.json()[0]
#         discord_name = str(ctx.message.author)
#         email = arg[0]
#         print(classroom_obj)
#         setSwearWordList()
# except Exception as e:
#     print(e)
#     await ctx.send("Please enter the email address associated with your account to link your account.")


@bot.command(name='mute')
async def mute(ctx):
    for x in ctx.message.guild.members:
        if x in ctx.message.author.voice.channel.members:
            if x == ctx.message.author:
                continue
            await x.edit(mute=True)
    await ctx.send("Rans is the big dumb!")


@bot.command(name='unmute')
async def unmute(ctx):
    for x in ctx.message.guild.members:
        if x in ctx.message.author.voice.channel.members:
            await x.edit(mute=False)
    await ctx.send("Rans is the big dumb!")


@bot.command(name='list')
async def list(ctx, *args):
    role = ""
    if len(args) != 0:
        role = args[0]

    if role != "":
        for x in ctx.message.guild.roles:
            if x.name == role:
                member_list = x.members
    else:
        member_list = ctx.message.guild.members

    text = '\n'.join(member.name for member in member_list)
    #text = "The number of students that are online right now are: 0. Ideally the output would be sorted in this priority: online/not online, alphabetical order."
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

    guild_reminders = reminders[ctx.guild]
    for reminder in guild_reminders:
        (datetime, message) = reminder
        text += str(i) + ":"
        text += " " + str(datetime)
        text += " " + "\"" + message + "\""
        text += "\n"
        i += 1

    await ctx.send(text)


@bot.command(name='reminder')
async def reminder(ctx, *args):
    # try:
    time = datetime.datetime.strptime(args[0] + " " + args[1], "%d/%m/%Y %H:%M:%S")
    print(time)

    global reminders
    if ctx.guild in reminders:
        reminders[ctx.guild] += [(time, args[2])]
    else:
        reminders[ctx.guild] = [(time, args[2])]
    await ctx.send("A reminder has been added.")
    print(reminders)
    # except:
    #     usage_text = "Usage:\n!reminder dd/mm/yyyy hh:mm:ss \"message\""
    #     await ctx.send(usage_text)
    #     return


@bot.command(name='removereminder')
async def removereminder(ctx, *args):
    try:
        index = int(args[0])
        global reminders
        guildreminders = reminders[ctx.guild]
        toremove = guildreminders[index]
        guildreminders.pop(index)

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


@bot.command(name='group')
async def group(ctx, *args):
    global groups

    mode = args[0]

    if mode == "dcreate":
        print("creating groups.")
        num_groups = int(args[1])
        basename = args[2] if len(args) >= 3 else "group"

        guild = ctx.message.guild
        for i in range(num_groups):
            admin_role = get(guild.roles, name="Admin")
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True),
                admin_role: discord.PermissionOverwrite(read_messages=True)
            }
            channel = await guild.create_text_channel(basename + "-" + str(i), overwrites=overwrites)
            groups.append(channel)
    elif mode == "dlist":
        text = "Active groups:\n"
        for (i, channel) in enumerate(groups):
            text += str(i) + ": " + str(channel) + "\n"

        await ctx.send(text)
    elif mode == "dremoveall":
        for channel in groups:
            await channel.delete()

        groups = []
    elif mode == "distributeall":
        guild = ctx.message.guild

        students = await getMembersOfRole(guild, Roles.STUDENT.value)

        per_group = len(students) // len(groups)
        remainder = len(students) % len(groups)

        for (groupnumber, group) in enumerate(groups):
            total = per_group + 1 if groupnumber < remainder else per_group

            for i in range(total):
                # add student
                student = students.pop()
                print("add " + str(student) + " to " + str(group))
                await group.set_permissions(student, read_messages=True, send_messages=True)
    elif mode == "move":
        # student = get_member_named(args[1])
        # group = groups[int(args[2])] // TODO STILL NEED TO REMOVE STUDENT FROM PREVIOUS GROUP.
        #
        # await group.set_permissions(student, read_messages=True, send_messages=True)

        pass


@bot.command(name='filter')
# @commands.has_role('Teacher')
async def filter(ctx, *args):
    global swearWords
    print(args)

    if (len(args) == 0):
        response = '\n'.join(swearWords)
    elif (args[0].lower() == "add"):
        print("hello")
        if (args[1] in swearWords):
            response = "This word is already being filtered."
        else:
            url = 'http://34.125.57.52/add/word/'
            headers = {'content-type': 'application/json'}
            x = requests.post(url, json={"discord_name": discord_name, "email": email, "word": {"word": args[1]}},
                              auth=(user, password), headers=headers)
            setSwearWordList()
            response = "This word has now been added to the filter."
    elif (args[0].lower() == "remove"):
        if (args[1] in swearWords):
            url = 'http://34.125.57.52/remove/word/'
            headers = {'content-type': 'application/json'}
            x = requests.post(url, json={"discord_name": discord_name, "email": email, "word": {"word": args[1]}},
                              auth=(user, password), headers=headers)
            setSwearWordList()
            response = "This word has been removed from the filer."
        else:
            response = "This word is not part of the filter."


    await ctx.send(response)


# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.errors.CheckFailure):
#         await ctx.send("Sorry, only the teacher can use that command.\n¯\_(ツ)_/¯")


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

    messageWords = message.content.split()
    print(messageWords)
    if any(word in messageWords for word in swearWords):
        print("bad")
        channel = await getChannel(message.guild, TextChannels.TEACHERS_LOUNGE.value)
        await channel.send(message.author.name + " (" + datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S") + "): " + message.content)
        await message.delete()
        response = "Please, do not use vulgar language.\nಠ_ಠ"
        await message.channel.send(response)

    try:
        await bot.process_commands(message)
    except:
        await message.channel.send("Improper use of command!")


@bot.event
async def on_ready():
    print('{client.user} has connected to Discord!')


def findWholeWord(w, input_str):
    return re.match(r'\b({0})\b'.format(w), input_str)
    # pattern = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def setSwearWordList():
    global swearWords, discord_name, email, user, password
    url = 'http://34.125.57.52/filterwords/'
    headers = {'content-type': 'application/json'}
    x = requests.post(url, json={"discord_name": discord_name, "email": email},
                      auth=(user, password), headers=headers)
    swearWords = []
    for y in x.json():
        swearWords.append(y["word"])

    print(swearWords)
    # parent_location = Path(__file__).absolute().parent
    # file_location = parent_location / 'swearWords.txt'
    # file = open(file_location)
    # swearWords = [line.rstrip('\n') for line in file]


@tasks.loop(seconds=1)
async def once_a_second():
    # check reminders
    global reminders
    currentdatetime = datetime.datetime.now()

    for guild in reminders:
        remove_reminders = []

        for reminder in reminders[guild]:
            (reminderdatetime, message) = reminder

            if reminderdatetime <= currentdatetime:
                print("Reminder! " + message)
                remove_reminders += [reminder]
                channel = await getChannel(guild, TextChannels.REMINDERS.value)
                await channel.send(message)

        reminders[guild] = [r for r in reminders[guild] if r not in remove_reminders]


@once_a_second.before_loop
async def before_once_a_second():
    await bot.wait_until_ready()


once_a_second.start()
bot.run(TOKEN)
