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

    # test whether loaded or not
    @commands.command(name="dean", hidden=True)
    @commands.is_owner()
    async def deaty(self, ctx):
        r = "dean loaded."
        await ctx.send(r)


    # TODO make permission bit fiddler. Four base levels:
    # Everyone, Accepted, Students, Teachers
    # From there the addition of permissions for classes would be ideal
    # 68608: Read Message, History, Send Message Only (everyone)
    # 67177473: Adds create invites and change nickname (accepted)
    # 67456065: Adds emojis, links, and reactions (student)
    # 470150211: Manage Roles, Kick Members, Attach Files, Manage Messages,
    # (teacher)

    # TODO make class creator. this would require a directory
    # structure and ground rules like creation, deletion, teacher

    # TODO make promotion/demotion def

def setup(bot):
    bot.add_cog(DeanCog(bot))
