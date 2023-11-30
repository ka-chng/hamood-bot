import discord
from discord.ext import commands
from discord.commands import slash_command

class help(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
    
    @slash_command(name = 'help', description = "Sends list of commands")
    @commands.cooldown(1, 5, commands.BucketType.user)  
    async def help(self, ctx):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        HelpEmbed1 = discord.Embed(title="Help Panel", description="Click on any of these buttons to get started", color=0xE2E26E)      
        view = help2()
        await ctx.respond(embed=HelpEmbed1, view=view)
class help2(discord.ui.View): 
    @discord.ui.button(label="GENERAL", style=discord.ButtonStyle.grey, emoji="<:GUS_ybthink:961369500387790958>")
    async def first_button_callback(self, button, interaction):
        HelpEmbed2 = discord.Embed(title="GENERAL",color=0xE2E26E) 
        HelpEmbed2.add_field(name="/profile", value="Shows the user profile", inline=True)
        HelpEmbed2.add_field(name="/animesearch", value="Searches for anime", inline=True)
        HelpEmbed2.add_field(name="/botinfo", value="Shows information about the bot", inline=True)
        HelpEmbed2.add_field(name="/help", value="Sends this command", inline=True)
        HelpEmbed2.add_field(name="/mangasearch", value="Searches for manga", inline=True)
        HelpEmbed2.add_field(name="/meme", value="Sends memes from r/memes", inline=True)
        HelpEmbed2.add_field(name="/messageinfo", value="Shows information about a message", inline=True)
        HelpEmbed2.add_field(name="/servericon", value="Shows the servers profile picture", inline=True)
        HelpEmbed2.add_field(name="/serverinfo", value="Shows information about the server", inline=True)
        HelpEmbed2.add_field(name="/simprate", value="Shows a users simprate", inline=True)
        await interaction.response.edit_message(embed=HelpEmbed2)
    @discord.ui.button(label="EMOTES", style=discord.ButtonStyle.grey, emoji="<:GUS_ybsunglasses:961369488610177085>")
    async def second_button_callback(self, button, interaction):
        HelpEmbed3 = discord.Embed(title="EMOTES",color=0xE2E26E)
        HelpEmbed3.add_field(name="/cry", value="Sends a random anime crying gif", inline=True)
        HelpEmbed3.add_field(name="/cuddle", value="Sends a random gif of two people cuddling", inline=True)
        HelpEmbed3.add_field(name="/feed", value="Sends a random gif of a anime character getting fed", inline=True)
        HelpEmbed3.add_field(name="/hug", value="Sends a random gif of two anime character hugging", inline=True)
        HelpEmbed3.add_field(name="/kiss", value="Sends a random gif of two anime character kissing", inline=True)
        HelpEmbed3.add_field(name="/pat", value="Sends a random gif of two anime character patting another anime character", inline=True)
        HelpEmbed3.add_field(name="/punch", value="Sends a random gif of two anime character punching another anime character", inline=True)
        HelpEmbed3.add_field(name="/poke", value="Sends a random gif of two anime character poking another anime character", inline=True)
        await interaction.response.edit_message(embed=HelpEmbed3)
    @discord.ui.button(label="ANIMALS", style=discord.ButtonStyle.grey, emoji="<:GUS_hearteyesplead:916268233353486386>")
    async def three_button_callback(self, button, interaction):
        HelpEmbed4 = discord.Embed(title="ANIMALS",color=0xE2E26E)
        HelpEmbed4.add_field(name="/dog", value="Sends random dog media taken from r/dogs", inline=True)
        HelpEmbed4.add_field(name="/cat", value="Sends random cat media taken from r/cats", inline=True)
        HelpEmbed4.add_field(name="/fox", value="Sends random fox media taken from r/fox", inline=True)
        HelpEmbed4.add_field(name="/bird", value="Sends random bird media taken from r/birds", inline=True)
        HelpEmbed4.add_field(name="/panda", value="Sends random panda media taken from r/pandas", inline=True)
        HelpEmbed4.add_field(name="/lizard", value="Sends random lizard media taken from r/lizards", inline=True)
        HelpEmbed4.add_field(name="/rabbit", value="Sends random rabbit media taken from r/rabbit", inline=True)
        await interaction.response.edit_message(embed=HelpEmbed4)
    @discord.ui.button(label="MODERATION", style=discord.ButtonStyle.grey, emoji="<:GUS_staff:918868772608155658>")
    async def four_button_callback(self, button, interaction):
        HelpEmbed5 = discord.Embed(title="MODERATION",color=0xE2E26E)
        HelpEmbed5.add_field(name="/report", value="Helps you report a bug found in the bot", inline=True)
        HelpEmbed5.add_field(name="/ban", value="Bans a user from the server", inline=True)
        HelpEmbed5.add_field(name="/kick", value="Kicks a user from the server", inline=True)
        HelpEmbed5.add_field(name="/mute", value="Mutes a user from the server", inline=True)
        HelpEmbed5.add_field(name="/modlog", value="Shows you how to setup modlog on the server", inline=True)
        HelpEmbed5.add_field(name="/purge", value="Deletes a number of messages ranging from 1-100", inline=True)
        await interaction.response.edit_message(embed=HelpEmbed5)

def setup(bot): 
   bot.add_cog(help(bot))