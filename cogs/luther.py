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
import sys
import requests
from discord.ext import commands
from dotenv import load_dotenv

# globals
logFILE = '/home/jeremy/codbot/logs/bots.log'
# sensitive globals
load_dotenv()
API_KEY = os.getenv('ESV_API_KEY')
API_URL = os.getenv('ESV_API_URL')


class LutherCog(commands.Cog):
    """LutherCog: knows things, looks cool."""

    # variables
    global API_KEY
    global API_URL

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="verse", help="Retrieves an ESV bible verse.")
    async def verse(self, ctx):

        global API_KEY
        global API_URL

        try:
            passage = 'John 3:16'
            params = {'q': passage,
                'include-headings': False,
                'include-footnotes': False,
                'include-verse-numbers': False,
                'include-short-copyright': False,
                'include-passage-references': False}

            headers = {'Authorization': 'Token %s' % API_KEY}

            response = requests.get(API_URL, params=params, headers=headers)
            passages = response.json()['passages']
            passage = passages[0].strip() if passages else 'Error: Not Found'
            await ctx.send(passage)
        except Exception as e:
            with open(logFILE, "a") as f:
                f.write(f'**ERROR: {type(e).__name__} - {e}\n')


    @commands.command(name="luther")
    async def lutty(self, ctx):
        r = "luther loaded."
        await ctx.send(r)


def setup(bot):
    bot.add_cog(LutherCog(bot))
