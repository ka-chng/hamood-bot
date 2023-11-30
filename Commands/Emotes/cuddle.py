import discord
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail, cuddle_gif

class cuddle(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'cuddle', description = "Cuddles with the mentioned user")
    @commands.cooldown(1, 5, commands.BucketType.user)  
    async def cuddle(self, ctx, member: discord.Member):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        cuddle_embed = discord.Embed(
            description=f"{ctx.author.name} cuddles with {member.name}",
            color=embed_color
)
        cuddle_embed.set_thumbnail(url=embed_thumbnail)
        cuddle_embed.set_image(url=random.choice(cuddle_gif))
        await ctx.respond(embed=cuddle_embed)

def setup(bot): 
   bot.add_cog(cuddle(bot)) 