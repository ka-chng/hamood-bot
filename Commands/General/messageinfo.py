import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class messageinfo(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'messageinfo', description = "Shows information about a message")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def messageinfo(self, ctx, message: discord.Message):
       print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
       message_embed = discord.Embed(
       title="Message information",
       color=embed_color
)
       message_id = message.id
       message_author = message.author
       message_sent = message.created_at
       message_channel = message.channel
       message_edited_at = message.edited_at
       
       message_embed.set_thumbnail(url=embed_thumbnail)
       message_embed.add_field(name="Message ID", value=message_id, inline=False)
       message_embed.add_field(name="Message Author", value=message_author, inline=False)
       message_embed.add_field(name="Message Sent", value=message_sent, inline=False)
       message_embed.add_field(name="Message Channel", value=f'<#{message_channel}>', inline=False)
       message_embed.add_field(name="Message Edited At", value=message_edited_at, inline=False)
       await ctx.respond(embed=message_embed)

def setup(bot): 
   bot.add_cog(messageinfo(bot)) 