import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot) :
        self.bot = bot
        
    moderation = discord.SlashCommandGroup("moderation", "Commands to moderate your server.")
    
    @moderation.command(name="kick", description="kicks a bad kitty from the server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member):
        await member.kick()
        await ctx.respond(f"{member} has been kicked from the server.")
        
    @moderation.command(name="ban", description="bans a bad kitty from the server")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason: str):
        await member.ban()
        await ctx.respond(f"{member} has been banned from the server.")
        
    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You do not have permission to use this command.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.respond("Member not found.")
        else:
            raise error
        
def setup(bot):
    bot.add_cog(Moderation(bot))