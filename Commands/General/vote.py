import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class vote(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'vote', description = "Sends the hamood vote link")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def vote(self, ctx):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        vote_embed = discord.Embed(
            title="Hamood Vote Link",
            description="[CLICK HERE](https://top.gg/bot/765938818527264769/vote)",
            color=embed_color
        )
        await ctx.respond(embed=vote_embed)

def setup(bot): 
   bot.add_cog(vote(bot)) 