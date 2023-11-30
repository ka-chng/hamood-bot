import discord
import datetime
from embed import embed_color, embed_thumbnail
from discord.ext import commands
from discord.commands import slash_command

class purge(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'purge', description = "Deletes messages")
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def purge(self, ctx, amount: int):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        if amount > 100:
            await ctx.respond("You can only delete up to 100 messages at a time")
            return
        await ctx.channel.purge(limit=amount)
        clear_embed = discord.Embed(color=embed_color)
        clear_embed.add_field(name='MESSAGES PURGED', value=f'{amount} message(s) have been purged', inline=False)
        clear_embed.add_field(name='ACTION LOG', value=f'This action was done by **{ctx.author.name}#{ctx.author.discriminator}** \n **STAFF ID** {ctx.author.id} ', inline=False)
        clear_embed.set_thumbnail(url=embed_thumbnail)
        await ctx.respond(embed=clear_embed, delete_after=3)
def setup(bot): 
   bot.add_cog(purge(bot))