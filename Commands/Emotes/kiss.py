import discord
import random
from discord.ext import commands
from discord.commands import slash_command
from embed import embed_color, embed_thumbnail, kiss_gif

class kiss(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
 
    @slash_command(name = 'kiss', description = "Kisses a mentioned user")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        kiss_embed = discord.Embed(
            description=f"{ctx.author.name} kisses {member.name}",
            color=embed_color
)
        kiss_embed.set_thumbnail(url=embed_thumbnail)
        kiss_embed.set_image(url=random.choice(kiss_gif))
        await ctx.respond(embed=kiss_embed)

def setup(bot):
   bot.add_cog(kiss(bot)) 