#!/usr/bin/env python
#
# Copyright: BSD 3 Clause License
# https://github.com/cartwright/scripts/blob/master/LICENSE
#
#   Author: Jeremy Cartwright
#  Contact: thebusker@hotmail.com
#  Created: Mon 27 Jan 2020 08:56:20 PM UTC
#  luther: knows things, loooks cool. That's what he does.

import os
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands


# globals
logFILE = "/home/jeremy/codbot/logs/bots.log"
# sensitive globals
load_dotenv()
API_KEY = os.getenv('ESV_API_KEY')
API_URL = os.getenv('ESV_API_URL')


class LutherCog(commands.Cog):
    """LutherCog: knows things, looks cool."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="verse", help="Retrieves an ESV bible verse.")
    async def verse(self, ctx, p: str):

        global API_KEY
        global API_URL
        global logFILE

        try:
            # wtf = p
            # passage = 'John 3:16'
            params = {'q': p,
                'include-headings': False,
                'include-footnotes': False,
                'include-verse-numbers': False,
                'include-short-copyright': False,
                'include-passage-references': False}

            headers = {'Authorization': 'Token %s' % API_KEY}

            response = requests.get(API_URL, params=params, headers=headers)
            passages = response.json()['passages']
            p = passages[0].strip() if passages else 'Error: Not Found'
            await ctx.send(p)
        except Exception as e:
            with open(logFILE, "a") as f:
                f.write(f'**ERROR: {type(e).__name__} - {e}\n')


    # test whether loaded or not
    @commands.command(name="luther", hidden=True)
    @commands.is_owner()
    async def lutty(self, ctx):
        r = "luther loaded. really."
        await ctx.send(r)


def setup(bot):
    bot.add_cog(LutherCog(bot))
