# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='vcm_')

@bot.command(name='join')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name='mute')
async def mute(ctx):
    channel = ctx.author.voice.channel
    for member in channel.members:
        await member.edit(mute=True)

@bot.command(name='unmute')
async def unmute(ctx):
    channel = ctx.author.voice.channel
    for member in channel.members:
        await member.edit(mute=False)

@bot.command(name='leave')
async def leave(ctx):
    await ctx.voice_client.disconnect()

print("Bot is running")
bot.run(TOKEN)