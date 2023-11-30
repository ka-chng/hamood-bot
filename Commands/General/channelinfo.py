import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class channelinfo(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'channelinfo', description = "Shows information about a text channel")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def channelinfo(self, ctx, channel: discord.TextChannel):
       print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
       channel_name = channel.id
       channel_id = channel.id
       channel_topic = channel.topic
       channel_created_at = channel.created_at
       channel_catergory = channel.category
       
       channel_info_embed = discord.Embed(
       title="CHANNEL INFO",
       color=embed_color
)    
       channel_info_embed.add_field(name="Channel Name", value=f'<#{channel_name}>', inline=False)
       channel_info_embed.add_field(name="Channel ID", value=channel_id, inline=False)
       channel_info_embed.add_field(name="Channel Topic", value=channel_topic, inline=False)
       channel_info_embed.add_field(name="Channel Created At", value=channel_created_at, inline=False)
       channel_info_embed.add_field(name="Channel Category", value=channel_catergory, inline=False)
       channel_info_embed.set_thumbnail(url=embed_thumbnail)
       await ctx.respond(embed=channel_info_embed)

def setup(bot): 
   bot.add_cog(channelinfo(bot)) 