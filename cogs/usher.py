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
import random
from discord.ext import commands
from cogs.lawrence import LawrenceCog
from cogs.luther import LutherCog
from tinydb import TinyDB, Query


# globals
logFILE = os.path.expanduser('codbot/logs/bots.log')
welcomeFILE = os.path.expanduser('codbot/data/welcome.txt')
screen = []

class UsherCog(commands.Cog):
    """UsherCog: a greeter/bouncer"""


    def __init__(self, bot):
        self.bot = bot

    # test whether loaded or not
    @commands.command(name="usher", hidden=True)
    @commands.is_owner()
    async def ushty(self, ctx):
        r = f"usher loaded."
        await ctx.send(r)


    # TODO make file w/ markdown for proper introduction
    # new user direct message
    async def on_member_join(member):
        await member.create_dm()
        with open(welcomeFILE, 'r') as f:
            welcome = f.read()
        await member.dm_channel.send(welcome)


    # TODO implement rules welcome page ala the Python discord
    # the !accept is key. Don't see anything but rules, then !accept


    # loads and caches screen
    async def loadScreen(self):
        # variables
        en = os.path.expanduser('codbot/data/en')
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
    async def threeStrikes(self, f: str, cID, mID):
        # variables
        m = await cID.fetch_message(mID)
        t = await LawrenceCog.getTime()
        u = Query()
        perp = {
            'user': str(m.author),
            'nick': str(m.author.display_name),
            'date': str(m.created_at),
            'message': str(m.content),
            'channel': str(m.channel)
        }
        # If at first you fail...
        try:
            # save offense in database, count priors
            perpDB = TinyDB(os.path.expanduser('codbot/data/perpDB.json'))
            perpDB.insert(perp)
            s = len(perpDB.search(u.user == perp['user']))
            perpDB.close()
            # call verse() on one of 19 verses re: importance of language
            with open(os.path.expanduser('codbot/data/swearScripture'), 'r') as f:
                    vrs = f.read().splitlines()
            v = random.choice(vrs)
            await LutherCog.verse(self, m, p=v)
            # Delete offending message. Still not sure bout this
            await m.delete()
        # gracefully handle exceptions
        except Exception as e:
            with open(logFILE, 'a') as f:
                f.write(f'USHER//threeStrikes//{e}//{t}\n')


    # checks messages to screen for profanity
    @commands.Cog.listener()
    async def on_message(self, message):
        # variables
        en = os.path.expanduser('codbot/data/en')
        t = await LawrenceCog.getTime()
        global screen
        flag = None
        # If at first you fail...
        try:
            # dont' reply to self
            if message.author.name == 'Usher':
                return
            # ensure list is populated
            if not screen:
                await self.loadScreen()
            # prep message for screening
            m = message.content.lower()
            words = m.split()
            # screen message
            for word in words:
                if word in screen:
                    flag = word
            # 3 strikes and you're out
            if flag:
                mID = message.id
                cID = message.channel
                await self.threeStrikes(flag, cID, mID)
        # gracefully handle exceptions
        except Exception as e:
            with open(logFILE, 'a') as f:
                f.write(f'USHER//on_message//{type(e)}//{e}//{t}\n')


    # TODO make custom help dialogue


def setup(bot):
    bot.add_cog(UsherCog(bot))
