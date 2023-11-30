import discord
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail, punch_gif

class punch(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'punch', description = "Punches a mentioned user")
    @commands.cooldown(1, 5, commands.BucketType.user)  
    async def punch(self, ctx, member: discord.Member):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        punch_embed = discord.Embed(
            description=f"{ctx.author.name} punches {member.name}",
            color=embed_color
)
        punch_embed.set_thumbnail(url=embed_thumbnail)
        punch_embed.set_image(url=random.choice(punch_gif))
        await ctx.respond(embed=punch_embed)

def setup(bot): 
   bot.add_cog(punch(bot)) 