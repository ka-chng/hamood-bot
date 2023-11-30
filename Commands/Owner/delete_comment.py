import discord
from discord.ext import commands
import os
import aiosqlite
from embed import embed_color, embed_thumbnail, owner_id
from discord.commands import slash_command


class delete_comment(commands.Cog): 
    def __init__(self, bot): 
        self.bot = bot

    @slash_command(name = 'delete_comment', description = "Deletes a comment from a users profile")
    async def delete_comment(ctx, user_id: int, comment: str):
        if ctx.author.id != owner_id:
            return await ctx.respond("You are not authorized to use this command")
        else:
            async with aiosqlite.connect('hamood.db') as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("DELETE FROM hamood WHERE user = ? AND comment = ?", (user_id, comment))
                    await conn.commit()
            await ctx.respond("Comment deleted")
        
    
def setup(bot):
    bot.add_cog(delete_comment(bot))