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
async def assign(ctx, *, role_name: str):
    if not ctx.guild:
        await ctx.send("This command can only be used in a server!")
        return
    
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    
    if not role:
        await ctx.send(f"Role '{role_name}' not found!")
        return
    
    try:
        await ctx.author.add_roles(role)
        await ctx.send(f"Successfully assigned the {role.name} role to {ctx.author.mention}!")
    except discord.Forbidden:
        await ctx.send("I don't have permission to assign this role!")
    except discord.HTTPException:
        await ctx.send("Failed to assign role. Please try again.")

mica.run(token, log_handler=handler, log_level=logging.DEBUG)