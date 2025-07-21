import discord
import aiohttp
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    fun = discord.SlashCommandGroup("fun", "all the fun commands :3")
    
    @fun.command(
        name='cat',
        description='sends a cute kitty',
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
    )
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
                data = await resp.json()
                image_url = data[0]["url"]
        embed = discord.Embed(title="kitty", description="meow", color=discord.Color.nitro_pink())
        embed.set_image(url=image_url)
        await ctx.respond(embed=embed)
        
    @fun.command(
        name='dog',
        description='sends a cute puppy',
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
    )
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                data = await resp.json()
                image_url = data["message"]
        embed = discord.Embed(title="puppy", description="woof", color=discord.Color.nitro_pink())
        embed.set_image(url=image_url)
        await ctx.respond(embed=embed)
        
    @fun.command(
        name="hug",
        description="hug someone if u cant irl",
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
    )
    async def hug(self, ctx, person: discord.Member):
        if person is None:
            await ctx.respond("Please mention a user to hug.")
            return
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://kawaii.red/api/gif/hug?token=anonymous") as resp:
                    if resp.status != 200:
                        await ctx.respond("something broke")
                        return
                    data = await resp.json()
                    image_url = data["response"]
        except aiohttp.ClientError:
            await ctx.respond("couldnt connect i make amazing code please try again later")
            return

        embed = discord.Embed(description=f"{ctx.author.mention} hugged {person.mention}!", color=discord.Color.nitro_pink())
        embed.set_image(url=image_url)
        await ctx.respond(embed=embed)
    
    
def setup(bot):
    bot.add_cog(Fun(bot))