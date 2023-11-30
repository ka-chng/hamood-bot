import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command
import sqlite3

class modlog(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        self.conn = sqlite3.connect('modlog.db')
        self.cursor = self.conn.cursor()
        
    @slash_command(name='modlog', description="Enables modlogs on the server")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def modlog(self, ctx, channel_name: discord.TextChannel):
        modlog_channel_name = channel_name.name
        guild_id = ctx.guild.id
        self.cursor.execute('SELECT channel_id FROM modlog WHERE guild_id = ?', (guild_id,))
        result = self.cursor.fetchone()
        if result:
            old_channel_id = result[0]
            self.cursor.execute('UPDATE modlog SET channel_id = ? WHERE guild_id = ?', (channel_name.id, guild_id))
            self.conn.commit()
            modlog_embed = discord.Embed(title="Modlog Channel Updated", color=embed_color)
            modlog_embed.add_field(name="Old Channel", value=f"<#{old_channel_id}>", inline=False)
            modlog_embed.add_field(name="New Channel", value=f"#{modlog_channel_name}", inline=False)
        else:
            self.cursor.execute('INSERT INTO modlog (guild_id, channel_id) VALUES (?, ?)', (guild_id, channel_name.id))
            self.conn.commit()
            modlog_embed = discord.Embed(title="Modlog Channel Set", color=embed_color)
            modlog_embed.add_field(name="Channel", value=f"#{modlog_channel_name}", inline=False)
        await ctx.respond(embed=modlog_embed)

def setup(bot): 
    bot.add_cog(modlog(bot))

