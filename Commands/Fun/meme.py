import discord
import aiohttp
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail

class meme(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'meme', description = "Sends a meme")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def meme(self, ctx):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
            meme_embed = discord.Embed(
        title="From r/memes",
        color=embed_color
    )    
        fortnite = res['data']['children'][random.randint(1, 25)]['data']['url']
        meme_embed.set_thumbnail(url=embed_thumbnail)
        meme_embed.set_image(url=fortnite)
        await ctx.respond(embed=meme_embed)

def setup(bot): 
   bot.add_cog(meme(bot)) 