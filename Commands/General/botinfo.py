import discord
from embed import embed_color, embed_thumbnail
from discord.ext import commands
from discord.commands import slash_command

class botinfo(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    @slash_command(name = 'botinfo', description = "Shows information about the bot")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def botinfo(self, ctx):
       print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
       bot_info_embed = discord.Embed(
       title='HAMOOD',
       color=embed_color
    )
       total_guilds = len(self.bot.guilds)   
       total_users = sum([len(guild.members) for guild in self.bot.guilds])    
       bot_info_embed.add_field(name="Developer", value='ka-ching#1515', inline=False)
       bot_info_embed.add_field(name="Support server", value='[ksc](https://discord.gg/7yFRDteqP3)', inline=False)
       bot_info_embed.add_field(name="Server Count", value=f'{total_guilds}', inline=False)
       bot_info_embed.add_field(name="Total Users", value=f"{total_users}", inline=False)
       bot_info_embed.set_thumbnail(url=embed_thumbnail)
       await ctx.respond(embed=bot_info_embed)
   


def setup(bot): 
   bot.add_cog(botinfo(bot)) 