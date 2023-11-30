import discord
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail, pat_gif

class pat(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'pat', description = "Pats a mentioned user")
    @commands.cooldown(1, 5, commands.BucketType.user)  
    async def pat(self, ctx, member: discord.Member):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        pat_embed = discord.Embed(
            description=f"{ctx.author.name} pats {member.name}",
            color=embed_color
)
        pat_embed.set_thumbnail(url=embed_thumbnail)
        pat_embed.set_image(url=random.choice(pat_gif))
        await ctx.respond(embed=pat_embed)

def setup(bot): 
   bot.add_cog(pat(bot)) 