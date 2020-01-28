#!/usr/bin/env python
#
# Copyright: BSD 3 Clause License
# https://github.com/cartwright/scripts/blob/master/LICENSE
#
#   Author: Jeremy Cartwright
#  Contact: thebusker@hotmail.com
#  Created: Mon 27 Jan 2020 08:55:00 PM UTC
#  dean: branch of codbot which deals with classes, students, and teachers

import discord
from discord.ext import commands


class DeanCog(commands.Cog):
    """DeanCog: primarily classes, students, and teachers"""


    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="dean")
    async def deaty(self, ctx):
        r = "dean loaded."
        await ctx.send(r)

def setup(bot):
    bot.add_cog(DeanCog(bot))
