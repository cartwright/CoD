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
from discord.ext import commands


class LawrenceCog(commands.Cog):
    """LawrenceCog: Practice the Presence of Christ"""


    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="lawrence")
    async def lawty(self, ctx):
        r = "lawrence loaded."
        await ctx.send(r)


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

""" # This works but is dangerous
    @bot.command(name="sweep", help="clears all messages in chat")
    async def sweep(ctx):
        # Clear messages in the chat
        await ctx.channel.purge()
"""

def setup(bot):
    bot.add_cog(LawrenceCog(bot))