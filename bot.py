#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord.abc import PrivateChannel
from discord.ext.commands import Bot
import asyncio
import random
import re
from vars import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='h-', help_command=None)

general = bot.get_channel(428689943637000206)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="with piss"))

@bot.event
async def on_message(message):
    if (('masspirg' in message.content.lower()) or ('mass pirg' in message.content.lower())):
        await masspirg_reaction(message)
    UMLCS = bot.get_guild(int(umlcs))
    if (message.guild == UMLCS):
        if ((message.channel.id == int(vergen)) or (message.channel.id == int(ephem)) or (message.channel.id == int(emo)) or (message.channel.id == int(verbot)) or (message.channel.id == int(flex))):
            await verified_reaction(message)
        else:
            await nonverified_reaction(message)
    else:
        await otherservers_reaction(message)
    await bot.process_commands(message)

@bot.command(name='say')
async def say(message, channelid, *, text):
    channel = bot.get_channel(int(channelid))
    if (message.author.id == 755142372827856946):
        await channel.send(text)
    else:
        if isinstance(message.channel, discord.abc.PrivateChannel):
            await message.channel.send('fuck you')


@bot.command(name='ping')
async def ping_hole(ctx):
    if ctx.author.id == bot.user.id:
        return
    ping_responses = ['hole', 'pong', 'i am CLEARLY the best bot on this server', 'mrpoopybutthole', 'holes before roles!', 'don\'t tell anyone i have a crush on cubemoji', hole, 'need hole', 'h o l e'] 
    response = random.choice(ping_responses) 
    await ctx.send(response)


@bot.command(name='help')
async def help_me(message):
    if message.author.id == bot.user.id:
        return
    await message.send('imagine needing help figuring out HoleBot...\nmy available commands are ``help``, ``say`` & ``ping``\nhowever don\'t use say or else')

@bot.event
async def verified_reaction(message):
    if (holev_e.match(message.content)) or (hole in message.content):
        await message.add_reaction(hole)
        await message.add_reaction(h)
        await message.add_reaction(o)
        await message.add_reaction(l)
        await message.add_reaction(e_emoji)
    if (pissv_e.match(message.content)) or (pisv_e.match(message.content)) or ("urine" in message.content):
        piss = bot.get_emoji(int(piss_id))
        await message.add_reaction(piss)
    if (cumv_e.match(message.content)) or (coomv_e.match(message.content)):
        cum = bot.get_emoji(int(cum_id))
        await message.add_reaction(cum)

@bot.event
async def nonverified_reaction(message):
    if (hole_e.match(message.content)) or (hole in message.content):
        await message.add_reaction(hole)
        await message.add_reaction(h)
        await message.add_reaction(o)
        await message.add_reaction(l)
        await message.add_reaction(e_emoji)

@bot.event
async def otherservers_reaction(message):
    if (hole_e.match(message.content)) or (hole in message.content):
        await message.add_reaction(hole)
        await message.add_reaction(h)
        await message.add_reaction(o)
        await message.add_reaction(l)
        await message.add_reaction(e_emoji)
    if (pissv_e.match(message.content)) or (pis_e.match(message.content)) or ("urine" in message.content):
        piss = bot.get_emoji(int(piss_id))
        await message.add_reaction(piss)
    if (cumv_e.match(message.content)) or (coom_e.match(message.content)):
        cum = bot.get_emoji(int(cum_id))
        await message.add_reaction(cum)

@bot.event
async def masspirg_reaction(message):
    await message.add_reaction(f_emoji)
    await message.add_reaction(u_emoji)
    await message.add_reaction(c_emoji)
    await message.add_reaction(k_emoji)
    await message.add_reaction(m_emoji)
    await message.add_reaction(a_emoji)
    await message.add_reaction(s_emoji)
    await message.add_reaction(dollar_emoji)
    await message.add_reaction(p_emoji)
    await message.add_reaction(i_emoji)
    await message.add_reaction(r_emoji)
    await message.add_reaction(g_emoji)

bot.run(TOKEN)
