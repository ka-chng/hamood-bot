import discord
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail, hug_gif

class hug(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    @slash_command(name = 'hug', description = "Hugs a mentioned user")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def hug(self, ctx, member: discord.Member):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        hug_embed = discord.Embed(
            description=f"{ctx.author.name} hugs {member.name}",
            color=embed_color
)
        hug_embed.set_thumbnail(url=embed_thumbnail)
        hug_embed.set_image(url=random.choice(hug_gif))
        await ctx.respond(embed=hug_embed)

def setup(bot): 
   bot.add_cog(hug(bot)) 