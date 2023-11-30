import aiosqlite
import discord
from embed import embed_color, embed_thumbnail
from discord.ext import commands

class on_ready(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name="/help!", type=1)
        await self.bot.change_presence(status=discord.Status.online, activity=activity)
        print(f"{self.bot.user} ready")
        print(f"Server count: {len(self.bot.guilds)}")
        # hamood table
        setattr(self.bot, "db", await aiosqlite.connect('hamood.db'))
        async with self.bot.db.cursor() as cursor:
            await cursor.execute("CREATE TABLE IF NOT EXISTS hamood (level INTEGER, xp INTEGER, user INTEGER, reputation INTEGER)")
        # comments table
        setattr(self.bot, "comments_db", await aiosqlite.connect('comments.db'))
        async with self.bot.comments_db.cursor() as cursor:
            await cursor.execute("CREATE TABLE IF NOT EXISTS comments (user INTEGER, sender_username TEXT, comment TEXT, date_sent DATE)")
        # modlog table
        setattr(self.bot, "modlog_db", await aiosqlite.connect('modlog.db'))
        async with self.bot.modlog_db.cursor() as cursor:
            await cursor.execute("CREATE TABLE IF NOT EXISTS modlog (guild_id INTEGER PRIMARY KEY, channel_id INTEGER)")

def setup(bot):
    bot.add_cog(on_ready(bot))
