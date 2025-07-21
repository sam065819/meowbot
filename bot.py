import dotenv
import discord
import os
import tomllib
from dotenv import load_dotenv
from discord.ext import commands

with open('config.toml', 'rb') as fileObj:
  config = tomllib.load(fileObj)

load_dotenv()
Intents = discord.Intents.default()
Intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=Intents)
    
guild_id = config["guild_id"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}') # type: ignore
    
@bot.slash_command(name='cat', description='meows')
async def cat(ctx):
    await ctx.respond('meow')
    
@bot.command()
async def sync(ctx):
    await bot.sync_commands()
    await ctx.send("Synced commands.")
    
bot.load_extension('cogs.moderation')
bot.run(os.getenv('TOKEN'))