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

hole = '\N{HOLE}'
h = '\U0001F1ED'
o = '\U0001F1F4'
l = '\U0001F1F1'
e_emoji = '\U0001F1EA'
f_emoji = '\U0001F1EB'
u_emoji = '\U0001F1FA'
c_emoji = '\U0001F1E8'
k_emoji = '\U0001F1F0'
m_emoji = '\U0001F1F2'
a_emoji = '\U0001F1E6'
s_emoji = '\U0001F1F8'
p_emoji = '\U0001F1F5'
i_emoji = '\U0001F1EE'
r_emoji = '\U0001F1F7'
g_emoji = '\U0001F1EC'
dollar_emoji = '\U0001F4B2'


smirk = '\U0001F60F'
heart = '\U0001F496'
yellow_heart = '\U0001F49B'
drips = '\U0001F4A6'

h_v = 'hHχ'
o_v = 'oOôòóôõöøÒÓÔÕÖØü0œòȯǒōõǫőốồṓṑȱṍȫỗṏǿȭǭỏơổọớờỡộởợ'
o_vv = 'oOyYôòóôõöøÒÓÔÕÖØü0œòȯǒōõǫőốồṓṑȱṍȫỗṏǿȭǭỏơổọớờỡộởợ'
l_v = 'lL1ḹḻḽλ'
e_v = 'eEëèéêËÈÊÉ3ėěĕēẽęȩɇếềḗḕễḝẻȅȇểẹḙḛệεⒺⓔ⒠'
p_v = 'PpπⓅⓟ⒫℗ṔṕṖṗƤƥⱣℙǷꟼ℘'
i_v = 'iI!1|ïÍÍíi̇́Ììi̇̀ĬĭÎîǏǐÏïḮḯĨĩi̇̃ĮįĮ́į̇́Į̃į̇̃ĪīĪ̀ī̀ỈỉȈȉI̋i̋ȊȋỊḬḭƗɨİiIıⒾⓘ⒤IiḬḭḮḯÍíÌìÎîÏïĨĩĪīĬĭĮįǏǐıƚⅈℹ'
s_v = 'sS$5ΣšßŠς'
double_s = 'ß'
c_v = 'ckKCĆćĈĉČčĊċC̄c̄ÇçḈḉȻȼƇƈɕƇ₡₢Ⓒⓒ⒞'
u_v = 'uUūŪúǔǓùÙŭŬûÛüÜůŮųŲũŨűŰȕȔṳṲṵṴṷṶṹṸṻṺ'
m_v = 'mMⓂⓜ⒨ḾḿṀṁṂṃꟿꟽⱮƜℳ'

hole_e = re.compile(r'.*(?<![A-z])+([\n\s]*)+['+h_v+']+([\s\n]*)+['+o_v+']+([\s\n]*)+['+l_v+']+([\s\n]*)+['+e_v+']+.*', re.MULTILINE)
piss_e = re.compile(r'.*(?<![A-z])+([\n\s]*)+['+p_v+']+([\s\n]*)+['+i_v+']+([\s\n]*)+['+s_v+']+([\s\n]*)+['+s_v+']+.*', re.MULTILINE)
pis_e = re.compile(r'.*(?<![A-z])+([\n\s]*)+['+p_v+']+([\s]*)+['+i_v+']+([\s\n]*)+['+double_s+']+.*', re.MULTILINE)
pee_e = re.compile(r'.*(?<![A-z])+([\n\s]*)+['+p_v+']+([\s]*)+['+e_v+']+([\s\n]*)+['+e_v+']+(?<![A-z])+.*', re.MULTILINE)
cum_e = re.compile(r'.*(?<![A-z])+([\n\s]*)+['+c_v+']+([\s\n]*)+['+u_v+']+([\s\n]*)+['+m_v+']+.*', re.MULTILINE)
coom_e = re.compile(r'.*(?<![A-z])+([\n\s]*)+['+c_v+']+([\s\n]*)+['+o_vv+']+([\s\n]*)+['+o_vv+']+([\s\n]*)+['+m_v+']+.*', re.MULTILINE)

holev_e = re.compile(r'.*(?<![wWcC])+([\n\s]*)+['+h_v+']+([\s\n]*)+['+o_v+']+([\s\n]*)+['+l_v+']+([\s\n]*)+['+e_v+']+.*', re.MULTILINE)
pissv_e = re.compile(r'.*([\n\s]*)+['+p_v+']+([\s\n]*)+['+i_v+']+([\s\n]*)+['+s_v+']+([\s\n]*)+['+s_v+']+.*', re.MULTILINE)
pisv_e = re.compile(r'.*([\n\s]*)+['+p_v+']+([\s]*)+['+i_v+']+([\s\n]*)+['+double_s+']+.*', re.MULTILINE)
peev_e = re.compile(r'.*(?<![A-z])+([\n\s]*)+['+p_v+']+([\s]*)+['+e_v+']+([\s\n]*)+['+e_v+']+(?<![A-z])+.*', re.MULTILINE)
cumv_e = re.compile(r'.*([\n\s]*)+['+c_v+']+([\s\n]*)+['+u_v+']+([\s\n]*)+['+m_v+']+.*', re.MULTILINE)
coomv_e = re.compile(r'.*([\n\s]*)+['+c_v+']+([\s\n]*)+['+o_vv+']+([\s\n]*)+['+o_vv+']+([\s\n]*)+['+m_v+']+.*', re.MULTILINE)

vergen = 803366782819237918
ephem = 803366987581095936 
emo = 803367390669701171
verbot = 806533217850884096
flex = 803367576599920640
umlcs = 428689943637000202

piss_id = 807400993246412821
cum_id = 807348408296800276