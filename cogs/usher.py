#!/usr/bin/env python
#
#  Copyright: BSD 3 Clause License
#  https://github.com/cartwright/scripts/blob/master/LICENSE
#
#   Author: Jeremy Cartwright
#  Contact: thebusker@hotmail.com
#  Created: Mon 27 Jan 2020 08:52:10 PM UTC
#  usher: greeter/bouncer

import os
import discord
from discord.ext import commands
from cogs.lawrence import LawrenceCog


# globals
logFILE = os.path.expanduser('codbot/logs/bots.log')
naughties = None

class UsherCog(commands.Cog):
    """UsherCog: a greeter/bouncer"""


    def __init__(self, bot):
        self.bot = bot

    # test whether loaded or not
    @commands.command(name="usher", hidden=True)
    @commands.is_owner()
    async def ushty(self, ctx):
        r = "usher loaded."
        await ctx.send(r)


    # TODO make file w/ markdown for proper introduction
    # new user direct message
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to Concord on Discord!'
        )


    # checks for naughties // right now is just silly...
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.name == 'Usher':
            return
        await message.channel.send(f'{message.author.name} lol')


    # TODO make custom help dialogue

"""
    # loads and caches naughties
    async def loadNaughties(screen = None):
        global naughties
        en = os.path.expanduser('codbot/en')
        t = await LawrenceCog.getTime()

        if not screen:
            try:
                with open(en) as f:
                    screen = readlines()
                    screen = [c.strip() for c in wordlist if c]
            except Exception as e:
                with open(logFILE, 'a') as f:
                    f.write(f'USHER//loadNaughties//{e}//{t}\n')
        naughties = screen


    # fetches naughties
    async def fetchNaughties():
        if not naughties:
            await loadNaughties()
        return naughties
"""


def setup(bot):
    bot.add_cog(UsherCog(bot))
