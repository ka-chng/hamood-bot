import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class ban(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    @slash_command(name = 'ban', description = "Bans a user from the guild")
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def ban(self, ctx, member: discord.Member, reason="No Reason specified"):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        if member == None:
            NoMentionEmbed = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}**, You need to mention a valid user to ban them from the guild")
            await ctx.respond(embed=NoMentionEmbed)
            
        else:
            guild = ctx.guild
            ban_embed = discord.Embed(title=f'USER BANNED', description=f'{member.mention} has been banned from the guild ', color=embed_color)
            ban_embed.add_field(name='ACTION LOG', value=f'This action was done by **{ctx.author.name}#{ctx.author.discriminator}**')
            ban_embed.add_field(name="REASON", value=reason, inline=False)
            ban_embed.set_thumbnail(url=embed_thumbnail)
            await ctx.respond(embed=ban_embed)
            await guild.ban(user=member)
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
                        mod_log_embed.add_field(name=f'USER BANNED', value=f'{member.mention} has been banned from the guild')
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
   bot.add_cog(ban(bot)) 