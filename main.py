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

preetthees_bot = commands.Bot(command_prefix='+=', intents=intents)


# Startup event
@preetthees_bot.event
async def on_ready():
    print(f"We are ready to go in, {preetthees_bot.user.name}")

@preetthees_bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!")

@preetthees_bot.event
async def on_message(message):
    if message.author == preetthees_bot.user:
        return
    
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} dont use that word!")
    
    await preetthees_bot.process_commands(message)

@preetthees_bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")

@preetthees_bot.command()
async def assign(ctx):
    role = discord.utils.get()

preetthees_bot.run(token, log_handler=handler, log_level=logging.DEBUG)