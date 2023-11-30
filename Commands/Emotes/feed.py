import discord
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail, feed_gif

class feed(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'feed', description = "Feeds a mentioned user")
    @commands.cooldown(1, 5, commands.BucketType.user)  
    async def feed(self, ctx, member: discord.Member):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        feed_embed = discord.Embed(
            description=f"{ctx.author.name} feeds {member.name}",
            color=embed_color
)
        feed_embed.set_thumbnail(url=embed_thumbnail)
        feed_embed.set_image(url=random.choice(feed_gif))
        await ctx.respond(embed=feed_embed)

def setup(bot): 
   bot.add_cog(feed(bot)) 