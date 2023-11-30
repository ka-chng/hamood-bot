import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command
import sqlite3

class kick(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        self.conn = sqlite3.connect('modlog.db')
        self.cursor = self.conn.cursor()

    @slash_command(name = 'kick', description = "Kicks a user from the guild")
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def kick(self, ctx, member: discord.Member, reason="No Reason specified"):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        if member == None:
            NoMentionEmbed = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}**, You need to mention a valid user to kick them from the guild")
            await ctx.respond(embed=NoMentionEmbed)
            
        else:
            guild = ctx.guild
            kick_embed = discord.Embed(title=f'USER KICKED', description=f'{member.mention} has been kicked from the guild', color=embed_color)
            kick_embed.add_field(name='ACTION LOG', value=f'This action was done by **{ctx.author.name}#{ctx.author.discriminator}**')
            kick_embed.add_field(name="REASON", value=reason, inline=False)
            kick_embed.set_thumbnail(url=embed_thumbnail)
            await ctx.respond(embed=kick_embed)
            await guild.kick(user=member)
            modlog_cog = self.bot.get_cog('modlog')
            if modlog_cog:
                guild_id = ctx.guild.id
                self.cursor.execute('SELECT channel_id FROM modlog WHERE guild_id = ?', (guild_id,))
                result = self.cursor.fetchone()
                if result:
                    channel_id = result[0]
                    modlog_channel = discord.utils.get(guild.channels, id=channel_id)
                    if modlog_channel:
                        mod_log_embed = discord.Embed(title="MODLOG", color=embed_color)
                        mod_log_embed.add_field(name=f'USER KICKED', value=f'{member.mention} has been kicked from the guild')
                        mod_log_embed.add_field(name="REASON", value=reason, inline=False)
                        mod_log_embed.add_field(name='MODERATOR', value=f'This action was done by **{ctx.author.name}#{ctx.author.discriminator}** \n\n **STAFF ID** \n {ctx.author.id} \n\n **CHANNEL** \n <#{ctx.channel.id}>', inline=False)
                        mod_log_embed.set_thumbnail(url=embed_thumbnail)
                        await modlog_channel.send(embed=mod_log_embed)
                    else:
                        print("Modlog channel not found")
                else:
                    print("Modlog channel not found")
            else:
                print("Modlog cog not found")

def setup(bot): 
   bot.add_cog(kick(bot)) 