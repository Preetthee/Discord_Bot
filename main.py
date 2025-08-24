import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

mica = commands.Bot(command_prefix='+=', intents=intents)


# Startup event
@mica.event
async def on_ready():
    print(f"We are ready to go in, {mica.user.name}")

@mica.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!")

@mica.event
async def on_message(message):
    if message.author == mica.user:
        return
    
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} dont use that word!")
    
    await mica.process_commands(message)

@mica.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")

@mica.command()
async def assign(ctx):
    role = discord.utils.get()

mica.run(token, log_handler=handler, log_level=logging.DEBUG)