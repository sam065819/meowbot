import dotenv
import discord
import os
import aiohttp
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
Intents = discord.Intents.default()
Intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=Intents)
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}') # type: ignore
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="cat videos"))
    
@bot.slash_command(
    name="ping",
    description="pong",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
async def ping(ctx):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(title="Pong!", description=f"Latency: {latency}ms", color=discord.Color.green())
    await ctx.respond(embed=embed)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def sync(ctx):
    await bot.sync_commands()
    await ctx.send("Synced commands.")
    
@sync.error
async def sync_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command.")
    else:
        raise error
    
    
bot.load_extension('cogs.moderation')
bot.load_extension('cogs.fun')
bot.run(os.getenv('TOKEN'))