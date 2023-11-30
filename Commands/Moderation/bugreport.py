import discord
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class bugreport(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'report', description = "Reports a bug found in the bot")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def bugreport(self, ctx, bug):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        bug_report_channel = self.bot.get_channel(946480940023152671)
        
        bug_report_embed1 = discord.Embed(
            title="Your Bug Report Has Been Submitted!",
            color=embed_color
        )
        bug_report_embed1.set_thumbnail(url=embed_thumbnail)
        bug_report_embed1.set_footer(text="Please be patient, you might be contacted by our staff members if we need to ask more questions")
        await ctx.respond(embed=bug_report_embed1)
        
        bug_report_embed2 = discord.Embed(
            title="Bug Report Received",
            color=embed_color
        )
        
        bug_report_embed2.set_thumbnail(url=embed_thumbnail)
        await bug_report_channel.send(embed=bug_report_embed2)
        
        bug_report_embed3 = discord.Embed(
            color=embed_color
        )
        bug_report_embed3.add_field(name ="Bug Reported By", value=f"{ctx.author.name}#{ctx.author.discriminator} \n ({ctx.author.id})", inline=False)
        bug_report_embed3.add_field(name ="Bug Description", value=f"{bug}", inline=False)
        bug_report_embed3.set_thumbnail(url=embed_thumbnail)
        await bug_report_channel.send(embed=bug_report_embed3)


def setup(bot): 
   bot.add_cog(bugreport(bot)) 