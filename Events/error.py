import discord
from embed import embed_color, embed_thumbnail
from discord.ext import commands

class error(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            missing_arg_embed = discord.Embed(title="You are missing required arguments", color=embed_color)
            missing_arg_embed.set_thumbnail(url=embed_thumbnail)
            await ctx.respond(embed=missing_arg_embed)

        elif isinstance(error, commands.errors.CommandNotFound):
            command_not_found_embed = discord.Embed(title="Command not found", color=embed_color)
            command_not_found_embed.set_thumbnail(url=embed_thumbnail)
            await ctx.respond(embed=command_not_found_embed)

        elif isinstance(error, commands.errors.BadArgument):
            bad_data_embed = discord.Embed(title="Data type passed is invalid", color=embed_color)
            bad_data_embed.set_thumbnail(url=embed_thumbnail)
            await ctx.respond(embed=bad_data_embed)
        

        elif isinstance(error, commands.errors.CheckFailure):
            no_permissions_embed = discord.Embed(title="You are missing the required permissions to use this command", color=embed_color)
            no_permissions_embed.set_thumbnail(url=embed_thumbnail)
            await ctx.respond(embed=no_permissions_embed)
        else:
            raise error
        
def setup(bot):
    bot.add_cog(error(bot))