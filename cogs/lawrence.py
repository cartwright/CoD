#!/usr/bin/env python
#
#  Copyright: BSD 3 Clause License
#  https://github.com/cartwright/scripts/blob/master/LICENSE
#
#   Author: Jeremy Cartwright
#  Contact: thebusker@hotmail.com
#  Created: Mon 27 Jan 2020 08:59:25 PM UTC
#  lawrence: a helper file for the CoDbot

import discord
import time
from discord.ext import commands


class LawrenceCog(commands.Cog):
    """LawrenceCog: Practice the Presence of Christ"""


    def __init__(self, bot):
        self.bot = bot

    # test whether loaded or not
    @commands.command(name="lawrence", hidden=True)
    @commands.is_owner()
    async def lawty(self, ctx):
        r = "lawrence loaded."
        await ctx.send(r)


    async def getTime():
        t = time.localtime()
        ctime = time.strftime('%H:%M:%S||%D')
        return ctime


    @commands.command(name="sweep", hidden=True)
    @commands.is_owner()
    async def sweep(self, ctx):
        # Clear messages in the chat
        await ctx.channel.purge()

"""
    # midnight counter TODO
    async def midnight():
        while True:
            if t in range(start, stop):
                sweep(self)

    # sweep a channel clean
    async def sweep(channel):
       await channel.purge()
       await chanel.send(f'{channel} has been swept. Good day.')
"""


def setup(bot):
    bot.add_cog(LawrenceCog(bot))
