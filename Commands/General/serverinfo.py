import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class serverinfo(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'serverinfo', description = "Shows information about the server")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def serverinfo(self, ctx):
       print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
       name = str(ctx.guild.name)
       owner = f'<@!{ctx.guild.owner_id}>'
       id = str(ctx.guild.id)
       member_count = str(ctx.guild.member_count)
       text_channels = len(ctx.guild.text_channels)
       voice_channels = len(ctx.guild.voice_channels)
       channels = text_channels + voice_channels
       verfication = str(ctx.guild.verification_level).upper()

       server_info_embed = discord.Embed(
       color=embed_color
)    
       server_info_embed.add_field(name="Owner", value=owner, inline=False)
       server_info_embed.add_field(name="Guild Name", value=name, inline=False)
       server_info_embed.add_field(name='Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=False)
       server_info_embed.add_field(name="Text channels", value=text_channels, inline=False)
       server_info_embed.add_field(name="Voice channels", value=voice_channels, inline=False)
       server_info_embed.add_field(name="Total channels", value=channels, inline=False)
       server_info_embed.add_field(name="Verfication level", value=verfication, inline=False)
       server_info_embed.add_field(name="Server ID", value=id, inline=False)
       server_info_embed.add_field(name="Member Count", value=member_count, inline=False)       
       await ctx.respond(embed=server_info_embed)

def setup(bot): 
   bot.add_cog(serverinfo(bot)) 