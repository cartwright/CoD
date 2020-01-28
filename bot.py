#!/usr/bin/env python
#
#  Copyright (c) 2012-2020 Jeremy Cartwright
#
#   Author: Jeremy Cartwright
#  Contact: thebusker@hotmail.com
#  Created: Mon 13 Jan 2020 12:52:40 PM CST
#  License: BSD-3-Clause
#  bot.py: a bot for a discord server bible study

import os
import discord
import sched
import time
from discord.ext import commands
from dotenv import load_dotenv


# globals
logFILE = "/home/jeremy/codbot/logs/bots.log"
cogsDIR = "/home/jeremy/codbot/cogs/"
studiesDIR = "/home/jeremy/codbot/studies/"
# sensitive globals
load_dotenv()
token = os.getenv('DISCORD_TOKEN')


# assign prefix
bot = commands.Bot(command_prefix='!')


# proof of successful connection and cog loading
@bot.event
async def on_ready():
    t = time.localtime()
    ctime = time.strftime("%H:%M:%S||%D", t)
    pid = os.getpid()
    initalCogs = ['cogs.usher',
                  'cogs.dean',
                  'cogs.luther',
                  'cogs.lawrence']

    if __name__ == '__main__':
        for cog in initalCogs:
            try: bot.load_extension(cog)
            except:
                with open(logFILE, "a") as f:
                    f.write(f'Failed to load {cog} @ {ctime}\n')
        with open(logFILE, "a") as f:
            f.write(f'{bot.user.name} has connected to Discord @ '
                    f'{ctime} on {pid}\n')


@bot.command(name="bot")
async def botty(ctx):
    r = "bot loaded."
    await ctx.send(r)


# handle events properly
@bot.event
async def on_command_error(ctx, error):
    t = time.localtime()
    ctime = time.strftime("%H:%M:%S||%D", t)
    e = error

    if isinstance(error, commands.errors.MissingRole):
        await ctx.send('You do not have the correct role for this command.'
                       '\n Type !help for a list of commands.')
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("I don't know how to do that. Type !help to see what "
                       "I can do.")
    else :
        with open(logFILE, "a") as f:
            f.write(f'{e}{ctime}\n')


# reload modules instead of killing codbot all the time...
@bot.command(name='reload', hidden=True)
@commands.is_owner()
async def CogReload(self, ctx, *, cog : str):
    """command which reloads a module.
    remember to use dot path, eg: cogs.luther"""

    try:
        self.bot.unload_extension(cog)
        self.bot.load_extension(cog)
    except Exception as e:
        await ctx.send('\N{PISTOL}')
        await ctx.send('{}: {}'.format(type(e).__name__, e))
    else:
        await ctx.send('\N{OK HAND SIGN}')


bot.run(token)
