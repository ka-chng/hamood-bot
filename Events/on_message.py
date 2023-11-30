import discord
from embed import embed_color, embed_thumbnail
from discord.ext import commands

class on_message(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    async def on_application_command_error(ctx, error, message):
        if isinstance(error, commands.CommandOnCooldown):
            cooldown_embed = discord.Embed(
            description="This command is currently in cooldown **[(5)]**",
            color=embed_color
    )
            await message.channel.send(embed=cooldown_embed)
        else:
            raise error  

    async def on_command_error(ctx, error, message):
        if isinstance(error, commands.CommandOnCooldown):
            cooldown_embed = discord.Embed(
            description="This command is currently in cooldown **[(5)]**",
            color=embed_color
    )
            await message.channel.send(embed=cooldown_embed)
        else:
            raise error
        
def setup(bot):
    bot.add_cog(on_message(bot))