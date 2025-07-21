import discord
import aiohttp
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    fun = discord.SlashCommandGroup("fun", "all the fun commands :3", integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },)
    
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
                        await ctx.respond("An error occurred, please try again")
                        return
                    data = await resp.json()
                    image_url = data["response"]
        except aiohttp.ClientError:
            await ctx.respond("Couldn't retrieve GIF. Please try again!")
            return

        embed = discord.Embed(description=f"{ctx.author.mention} hugged {person.mention}!", color=discord.Color.nitro_pink())
        embed.set_image(url=image_url)
        await ctx.respond(embed=embed)
    
    @fun.command(
        name="cuddle",
        description="cuddles someone :D",
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
    )
    async def cuddle(self, ctx, person: discord.Member):
        if person is None:
            await ctx.respond("Please mention a person :3")
            return
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://kawaii.red/api/gif/cuddle?token=anonymous") as resp:
                    if resp.status != 200:
                        await ctx.respond("An error occurred, please try again")
                        return
                    data = await resp.json()
                    image_url = data["response"]
        except aiohttp.ClientError:
            await ctx.respond("Couldn't retrieve GIF. Please try again!")
            return
        
        embed = discord.Embed(description=f"{ctx.author.mention} cuddles {person.mention}!", color=discord.Color.nitro_pink())
        embed.set_image(url=image_url)
        await ctx.respond(embed=embed)
        
    @fun.command(
        name="cry",
        description="show someone you're sad",
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
    )
    async def cry(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.otakugifs.xyz/gif?reaction=cry") as resp:
                    if resp.status != 200:
                        await ctx.respond("An error occurred, please try again")
                        return
                    data = await resp.json()
                    image_url = data["url"]
        except aiohttp.ClientError:
            await ctx.respond("Couldn't retrieve GIF. Please try again!")
            return
        
        embed = discord.Embed(description=f"Aww, {ctx.author.mention} is crying :(", color=discord.Color.nitro_pink())
        embed.set_image(url=image_url)
        await ctx.respond(embed=embed)  
        
        
    @fun.command(
        name="8ball",
        description="seek an answer from the 8 ball",
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
    )
    async def ball(self, ctx, question: str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://eightballapi.com/api") as resp:
                    data = await resp.json()
                    response = data["reading"]
        except aiohttp.ClientError:
            embed = discord.Embed(title=f"{question}", description="8 ball answers: Cannot decide, try again later", color=discord.Color.red())
            await ctx.respond(embed=embed)
        embed = discord.Embed(title=f"{question}", description=f"8 ball answers: {response}", color=discord.Color.green())
        await ctx.respond(embed=embed) 
    @fun.command(
        name="happy",
        description="show someone you're happy",
        integration_types={
            discord.IntegrationType.guild_install,
            discord.IntegrationType.user_install,
        },
    )
    async def happy(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.otakugifs.xyz/gif?reaction=happy") as resp:
                    if resp.status != 200:
                        await ctx.respond("An error occurred, please try again")
                        return
                data = await resp.json()
                image_url = data["response"]
        except aiohttp.ClientError:
            await ctx.respond("Couldn't retrieve GIF. Please try again!")
            return
        embed = discord.Embed(description=f"Yay! {ctx.author.mention} is happy!", color=discord.Color.nitro_pink())
        embed.set_image(url=image_url)
        await ctx.respond(embed=embed)
                
    
def setup(bot):
    bot.add_cog(Fun(bot))