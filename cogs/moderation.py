import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot) :
        self.bot = bot
        
    @discord.slash_command()
    async def kick(self, ctx, member: discord.Member, reason: str):
        discord.Member.kick(member, reason)
        await ctx.respond("User ", member, "has been kicked for ", reason)
        
def setup(bot):
    bot.add_cog(Moderation(bot))