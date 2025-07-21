import discord
import bot
from bot import guild_id
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot) :
        self.bot = bot
        
    moderation = discord.SlashCommandGroup("moderation", "Commands to moderate your server.")
    
    @moderation.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member):
        await member.kick()
        await ctx.respond(f"{member} has been kicked from the server.")
        
    @moderation.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason: str):
        await member.ban()
        await ctx.respond(f"{member} has been banned from the server.")
        
def setup(bot):
    bot.add_cog(Moderation(bot))