import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class subcounter(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'subcounter', description = "Shows a youtubers subscriber count")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def sub(self, ctx, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        sub_count_elem = soup.find("yt-formatted-string", {"class": "style-scope ytd-c4-tabbed-header-renderer"})
        sub_count = sub_count_elem.text.strip()
        await ctx.respond(f"Sub count for {url}: {sub_count}")

def setup(bot): 
   bot.add_cog(subcounter(bot)) 
