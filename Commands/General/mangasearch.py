import discord
import requests
from discord.ext import commands
from embed import embed_color, embed_thumbnail
from discord.commands import slash_command

class mangasearch(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'mangasearch', description = "Searches for manga")
    async def mangasearch(self, ctx, *, arg):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        argument = str(arg)
        results = requests.get(f"https://api.jikan.moe/v3/search/manga?q={argument}&limit=1")
        for i in results.json()["results"]:
         manga_embed=discord.Embed(title=f'{i["title"]}', url=f'{i["url"]}', description=f'{i["synopsis"]}\n\n**Rating: ** {i["score"]}\n**Chapters: ** {i["chapters"]}', color=embed_color)
         manga_embed.set_thumbnail(url=embed_thumbnail)
         manga_embed.set_image(url=f'{i["image_url"]}')
        await ctx.respond(embed=manga_embed)

def setup(bot): 
   bot.add_cog(mangasearch(bot)) 