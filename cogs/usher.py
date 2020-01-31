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
screen = []

class UsherCog(commands.Cog):
    """UsherCog: a greeter/bouncer"""


    def __init__(self, bot):
        self.bot = bot

    # test whether loaded or not
    @commands.command(name="usher", hidden=True)
    @commands.is_owner()
    async def ushty(self, ctx):
        r = f"usher loaded. {screen[3]}"
        await ctx.send(r)


    # TODO make file w/ markdown for proper introduction
    # new user direct message
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to Concord on Discord!'
        )


    # loads and caches screen
    async def loadScreen(self):
        # variables
        en = os.path.expanduser('codbot/en')
        t = await LawrenceCog.getTime()
        global screen
        # populate screen
        try:
            with open(en, 'r') as f:
                screen = f.readlines()
                screen = [c.strip() for c in screen]
        # gracefully handle exceptions
        except Exception as e:
            with open(logFILE, 'a') as f:
                f.write(f'USHER//loadScreen//{e}//{t}\n')


    # tabulates history of repeat offenders
    # is sending name of channel, need to define it
    async def threeStrikes(self, chan, f: str):
        await chan.send(f'{f} is prohibited.')

    # checks for naughties // right now is just silly...
    # getting closer. need to use regex. why won't loadScreen() work?
    @commands.Cog.listener()
    async def on_message(self, message):
        # variables
        en = os.path.expanduser('codbot/en')
        t = await LawrenceCog.getTime()
        global screen
        flag = None
        chan = message.channel
        # dont' reply to self
        try:
            if message.author.name == 'Usher':
                return
            # ensure list is populated
            if not screen:
                await self.loadScreen()
            # prep message for screening
            m = message.content
            words = m.split()
            # screen message
            for word in words:
                if word in screen:
                    flag = word
            # 3 strikes and you're out
            if flag:
                #await self.threeStrikes(flag, chan)
                await message.channel.send(f'{flag} is prohibited')
        # gracefully handle exceptions
        except Exception as e:
            with open(logFILE, 'a') as f:
                f.write(f'USHER//on_message//{e}//{t}\n')


    # TODO make custom help dialogue


def setup(bot):
    bot.add_cog(UsherCog(bot))
