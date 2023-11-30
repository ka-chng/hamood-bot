import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class servericon(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    @slash_command(name = 'servericon', description = "Shows the icon of the server")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def servericon(self, ctx):
       print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
       server_icon_embed = discord.Embed(
       description=f"Server icon for **{ctx.guild.name}**",
       color=embed_color
)    
       icon = str(ctx.guild.icon.url)
       server_icon_embed.set_image(url=icon)
       server_icon_embed.set_thumbnail(url=embed_thumbnail)       
       await ctx.respond(embed=server_icon_embed)

def setup(bot): 
   bot.add_cog(servericon(bot)) 