import dotenv
import discord
import os
import tomllib
import aiohttp
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
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
            data = await resp.json()
            image_url = data[0]["url"]
    embed = discord.Embed(title="kitty", description="meow", color=discord.Color.nitro_pink())
    embed.set_image(url=image_url)
    await ctx.respond(embed=embed)
    
@bot.command()
async def sync(ctx):
    await bot.sync_commands()
    await ctx.send("Synced commands.")
    
bot.load_extension('cogs.moderation')
bot.run(os.getenv('TOKEN'))