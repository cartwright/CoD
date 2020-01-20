#!/usr/bin/env python
#
#  Copyright (c) 2012-2020 Jeremy Cartwright
#
#   Author: Jeremy Cartwright
#  Contact: thebusker@hotmail.com
#  Created: Mon 13 Jan 2020 12:52:40 PM CST
#  License: BSD-3-Clause
#  Usher: a bot for a discord server to act as greeter/bouncer

import os
import discord
import datetime
from discord.ext import commands
from dotenv import load_dotenv

# globals
log = "/home/jeremy/bots/logs/bots.log"

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')


# proof of successful connection
@bot.event
async def on_ready():
    now = datetime.datetime.now().timestamp()
    pid = os.getpid()
    with open(log, "a") as f:
        f.write(f'{bot.user.name} has connected to Discord @ '
                f'{now} on {pid}\n')


# handle events properly
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send('You do not have the correct role for this command.'
                       '\n Type !help for a list of commands.')
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("I don't know how to do that. Type !help to see what "
                       "I can do.")
    else :
        with open(log, "a") as f:
            f.write(str(discord.DiscordException)+"\n")


# daily sweep of the lobby
#sync def on_days_end(ctx):
    # at the stroke of midnight
#   lobby = ctx.message.guild.TextChannel.name
#   await lobby.purge()
#   await lobby.send('The Lobby has been swept. Good morning.')

@bot.command(name="sweep", help="clears all messages in chat")
async def sweep(ctx):
    # Clear messages in the chat
    await ctx.channel.purge()

# new user direct message
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Concord on Discord!'
    )


# screen for naughties
@bot.event
async def on_teh_naughty(message):
#naughty = open('en').read().splitlines()

    # print message content
    await message.content


bot.run(token)
