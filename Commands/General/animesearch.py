import discord
import requests
from embed import embed_color, embed_thumbnail
from discord.ext import commands

from discord.commands import slash_command

class animesearch(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot
        
    @slash_command(name = 'animesearch', description = "Searches for anime")
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def animesearch(self, ctx, *, anime_name):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        argument = str(anime_name)
        results = requests.get(f"https://api.jikan.moe/v3/search/anime?q={argument}&limit=1")
        if results.status_code == 200:
            anime_data = results.json()["results"][0]
            anime_embed = discord.Embed(title=f'{anime_data["title"]}', url=f'{anime_data["url"]}', description=f'{anime_data["synopsis"]}\n\n**Rating: ** {anime_data["score"]}\n**Episodes:** {anime_data["episodes"]}', color=embed_color)
            anime_embed.set_thumbnail(url=embed_thumbnail)
            anime_embed.set_image(url=f'{anime_data["image_url"]}')
            await ctx.respond(embed=anime_embed)
        else:
            await ctx.respond("No results found for the given anime")

def setup(bot): 
   bot.add_cog(animesearch(bot))
