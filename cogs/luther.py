#!/usr/bin/env python
#
# Copyright: BSD 3 Clause License
# https://github.com/cartwright/scripts/blob/master/LICENSE
#
#   Author: Jeremy Cartwright
#  Contact: thebusker@hotmail.com
#  Created: Mon 27 Jan 2020 08:56:20 PM UTC
#  luther: knows things, loooks cool. That's what he does.

import discord
from discord.ext import commands


class LutherCog(commands.Cog):
    """LutherCog: knows things, looks cool."""


    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="luther")
    async def lutty(self, ctx):
        r = "luther loaded."
        await ctx.send(r)


def setup(bot):
    bot.add_cog(LutherCog(bot))
