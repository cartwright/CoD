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
from discord.ext import commands
from dotenv import load_dotenv
from cogs.lawrence import LawrenceCog


# globals
logFILE = os.path.expanduser('codbot/logs/bots.log')
# sensitive globals
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# assign prefix
bot = commands.Bot(command_prefix='!')


# proof of successful connection and cog loading
@bot.event
async def on_ready():
    t = await LawrenceCog.getTime()
    pid = os.getpid()
    initalCogs = ['cogs.usher',
                  'cogs.dean',
                  'cogs.luther',
                  'cogs.lawrence']

    if __name__ == '__main__':
        for cog in initalCogs:
            try: bot.load_extension(cog)
            except Exception as e:
                with open(logFILE, "a") as f:
                    f.write(f'Failed to load {cog} @ {t}\n'
                           f'{e}\n')
        with open(logFILE, "a") as f:
            f.write(f'{bot.user.name} has connected to Discord @ '
                    f'{t} on {pid}\n')


# test whether loaded or not
@bot.command(name="bot", hidden=True)
@commands.is_owner()
async def botty(ctx):
    r = "bot loaded."
    await ctx.send(r)


# handle events properly
@bot.event
async def on_command_error(ctx, error):
    t = await LawrenceCog.getTime()
    e = error

    if isinstance(error, commands.errors.MissingRole):
        await ctx.send('You do not have the correct role for this command.'
                       '\n Type !help for a list of commands.')
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("I don't know how to do that. Type !help to see what "
                       "I can do.")
    else :
        with open(logFILE, "a") as f:
            f.write(f'BOT//on_command_error//{e}//{t}\n')


# reload modules instead of killing codbot all the time...
@bot.command(name='reload', hidden=True)
@commands.is_owner()
async def cogReload(self, cog: str):
    """command which reloads a module.
    remember to use dot path, eg: cogs.luther"""

    t = await LawrenceCog.getTime()

    global logFILE

    try:
        self.bot.reload_extension(cog)
    except Exception as e:
        with open(logFILE, "a") as f:
            await f.write(f'BOT//cogReload//{e}//{t}\n')


# shutdown bot
@bot.command(name='quit', hidden=True)
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()


bot.run(TOKEN)
