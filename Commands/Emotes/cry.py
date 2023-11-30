import discord
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail, cry_gif

class cry(commands.Cog):     

    def __init__(self, bot): 
        self.bot = bot
    
    @slash_command(name = 'cry', description = "Sends a crying gif")
    @commands.cooldown(1, 5, commands.BucketType.user)  
    async def cry(self, ctx):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        cry_embed = discord.Embed(
            description=f"{ctx.author.name} cries",
            color=embed_color
)
        cry_embed.set_thumbnail(url=embed_thumbnail)
        cry_embed.set_image(url=random.choice(cry_gif))
        await ctx.respond(embed=cry_embed)

def setup(bot): 
   bot.add_cog(cry(bot)) 