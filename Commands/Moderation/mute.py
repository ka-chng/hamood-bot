import discord
import datetime
from embed import embed_color, embed_thumbnail
from discord.ext import commands
from discord.commands import slash_command

class mute(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
    
    @slash_command(name = 'mute', description = "Mutes a mentioned user")
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def mute(self, ctx, member: discord.Member, minutes: int, reason="No Reason specified"):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        duration = datetime.timedelta(minutes=minutes)
        mute_embed = discord.Embed(color=embed_color)
        mute_embed.add_field(name='USER MUTED', value=f'{member.mention} has been muted for {minutes} minutes', inline=False)
        mute_embed.add_field(name='ACTION LOG', value=f'This action was done by **{ctx.author.name}#{ctx.author.discriminator}**', inline=False)
        mute_embed.add_field(name="REASON", value=reason, inline=False)
        mute_embed.set_thumbnail(url=embed_thumbnail)
        await member.timeout_for(duration)
        await ctx.respond(embed=mute_embed)
       
        mod_log_embed = discord.Embed(title="MODLOG", color=embed_color)
        mod_log_embed.add_field(name='USER MUTED', value=f'{member.mention} has been muted for {minutes} minutes', inline=False)
        mod_log_embed.add_field(name="REASON", value=reason, inline=False)
        mod_log_embed.add_field(name='MODERATOR', value=f'This action was done by **{ctx.author.name}#{ctx.author.discriminator}** \n\n **STAFF ID** \n {ctx.author.id} \n\n **CHANNEL** \n <#{ctx.channel.id}>', inline=False)
        mod_log_embed.set_thumbnail(url=embed_thumbnail)
        modlog_cog = self.bot.get_cog('modlog')
        if modlog_cog:
            channel_id = modlog_cog.modlog_channels.get(ctx.guild.id)
            if channel_id:
                channel = discord.utils.get(ctx.guild.channels, id=channel_id)
                if channel:
                    await channel.send(embed=mod_log_embed)

def setup(bot): 
   bot.add_cog(mute(bot)) 
