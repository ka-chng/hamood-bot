import discord
from discord.ext import commands
import os
from embed import embed_color, embed_thumbnail, owner_id
from discord.commands import slash_command

class reload_cogs(commands.Cog): 
    def __init__(self, bot): 
        self.bot = bot

    @slash_command(name = 'reload', description = "Reloads a cog from the gbot")
    async def reload(self, ctx, extension):
        if ctx.author.id != owner_id:
            return await ctx.respond(
            "Only the bot developer can use this command") 
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.bot.reload_extension(extension)
            reload_cog_embed = discord.Embed(title="Cog Reloaded", color=embed_color)
            await ctx.respond(embed=reload_cog_embed)
            
def setup(bot):
    bot.add_cog(reload_cogs(bot))