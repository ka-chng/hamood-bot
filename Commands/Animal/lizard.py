import discord
import aiohttp
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail

class lizard(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'lizard', description = "Sends random media of lizard\'s taken from r/lizard")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def lizard(self, ctx):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/lizards/new.json?sort=hot') as r:
                res = await r.json()
            lizard_embed = discord.Embed(
            color=embed_color
        )       
        lizard_embed.set_thumbnail(url=embed_thumbnail)
        fortnite = res['data']['children'][random.randint(1, 15)]['data']['url']
        if ctx.channel.is_nsfw():
            await ctx.respond(embed=lizard_embed)
        else:
            await ctx.respond('To prevent any issues since these images are taken from subreddit\'s you can only use the animal commands in NSFW chats')

def setup(bot): 
   bot.add_cog(lizard(bot)) 