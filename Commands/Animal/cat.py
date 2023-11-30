import discord
import aiohttp
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail

class cat(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'cat', description = "Sends a random picture of a cat")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def cat(self, ctx):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/cat/new.json?sort=hot') as r:
                res = await r.json()
                cat_embed = discord.Embed(
                color=embed_color
            )    
        cat_embed.set_thumbnail(url=embed_thumbnail)
        fortnite = res['data']['children'][random.randint(1, 25)]['data']['url']
        if ctx.channel.is_nsfw():
            await ctx.respond(embed=cat_embed)
        else:
            await ctx.respond('To prevent any issues since these images are taken from subreddit\'s you can only use the animal commands in NSFW chats')
def setup(bot): 
   bot.add_cog(cat(bot)) 