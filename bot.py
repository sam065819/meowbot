import dotenv
import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    
@bot.slash_command(name='cat', description='meows')
async def cat(ctx):
    await ctx.respond('meow')
    

bot.run(os.getenv('TOKEN'))
bot.load_extension('cogs.moderation')