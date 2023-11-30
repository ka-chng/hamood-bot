import discord
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail, poke_gif

class poke(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
      
    @slash_command(name = 'poke', description = "Pokes a mentioned user")
    @commands.cooldown(1, 5, commands.BucketType.user)  
    async def poke(self, ctx, member: discord.Member):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        poke_embed = discord.Embed(
            description=f"{ctx.author.name} pokes {member.name}",
            color=0xE2E26E
)
        poke_embed.set_thumbnail(url=embed_thumbnail)
        poke_embed.set_image(url=random.choice(poke_gif))
        await ctx.respond(embed=poke_embed)

def setup(bot): 
   bot.add_cog(poke(bot)) 