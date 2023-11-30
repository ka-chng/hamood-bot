import discord
import aiohttp
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail

class rabbit(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'rabbit', description = "Sends random media of rabbit\'s taken from r/bunnies")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def rabbit(self, ctx):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/bunnies/new.json?sort=hot') as r:
                res = await r.json()
            rabbit_embed = discord.Embed(
        color=embed_color
)    
        rabbit_embed.set_thumbnail(url=embed_thumbnail)
        fortnite = res['data']['children'][random.randint(1, 25)]['data']['url']
        if ctx.channel.is_nsfw():
            await ctx.respond(embed=rabbit_embed)
        else:
            await ctx.respond('To prevent any issues since these images are taken from subreddit\'s you can only use the animal commands in NSFW chats')

def setup(bot): 
   bot.add_cog(rabbit(bot)) 