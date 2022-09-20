# This example requires the 'message_content' intent.

import logging
import discord
from discord.ext import commands
from mwclient import Site

logging.basicConfig(level=logging.WARNING)

description = '''This is a description.'''
intents = discord.Intents.default()
intents.message_content = True

tokenfile = open("G:\programming fun\wish.txt", "r") #change path to wherever token is located
token = tokenfile.read()
tokenfile.close()

site = Site('wiki.gbl.gg', path='/')

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def length(ctx):
    await ctx.send(f'Your message is {len(ctx.message.content)} characters long.')

@bot.command()
async def fd(ctx, moveId: str):
    result = site.api('cargoquery', tables='UNICLR_MoveData', fields='UNICLR_MoveData.moveId, UNICLR_MoveData.damage', where='moveId="%s"' % moveId)
    for page in result['cargoquery'][0].values():
        await ctx.send(f'{moveId} damage is {page["damage"]}')

bot.run(token)
