import discord
from discord.commands import slash_command
from discord.ui import Button, View
import asyncio
from sqlalchemy import desc
from embed import embed_color, embed_thumbnail
import aiosqlite
from discord.ext import commands
import datetime

class ReputationView(View):
    def __init__(self, bot, user_id):
        super().__init__()
        self.bot = bot
        self.user_id = user_id
        self.reputation_given = False

    @discord.ui.button(label='+rep', style=discord.ButtonStyle.green)
    async def plus_rep(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user_id:
            await interaction.response.send_message("You can't give reputation points to yourself", ephemeral=True)
            return
        
        if self.reputation_given:
            await interaction.response.send_message("You have already given reputation to this profile", ephemeral=True)
            return

        async with aiosqlite.connect('hamood.db') as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("UPDATE hamood SET reputation = reputation + 1 WHERE user = ?", (str(self.user_id),))
                await conn.commit()

        self.reputation_given = True
        await interaction.response.send_message("Reputation point added", ephemeral=True)

    @discord.ui.button(label='-rep', style=discord.ButtonStyle.red)
    async def minus_rep(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id == self.user_id:
            await interaction.response.send_message("You can't remove reputation points from yourself", ephemeral=True)
            return

        async with aiosqlite.connect('hamood.db') as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("UPDATE hamood SET reputation = reputation - 1 WHERE user = ?", (str(self.user_id,)))
                await conn.commit()

        await interaction.response.send_message("Reputation point removed", ephemeral=True)
    
    
    @discord.ui.button(label='Show Comments', style=discord.ButtonStyle.green)
    async def show_comments(self, button: discord.ui.Button, interaction: discord.Interaction):
        async with aiosqlite.connect('comments.db') as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT sender_username, comment, date_sent FROM comments WHERE user = ?", (self.user_id,))
                comments = await cursor.fetchall()

        comments_embed = discord.Embed(
            description=f"<@!{self.user_id}>'s Comments",
            color=embed_color
        )
        if len(comments) == 0:
            comments_embed.add_field(name="No Comments", value="There are no comments to display", inline=False)
        else:
            for comment in comments:
                if comment[2] is None:
                    comment_text = f"{comment[1]} - No Date"
                else:
                    try:
                        comment_date = datetime.datetime.fromisoformat(comment[2])
                        comment_text = f"{comment[1]} - {comment_date.strftime('%Y-%m-%d')}"
                    except ValueError:
                        comment_text = f"{comment[1]} - Invalid Date"
                comments_embed.add_field(name=comment[0], value=comment_text, inline=False)

        await interaction.response.send_message(embed=comments_embed)

    @discord.ui.button(label='Add Comment', style=discord.ButtonStyle.green)
    async def add_comment(self, button: discord.ui.Button, interaction: discord.Interaction):
        def check(m):
            return m.author.id == interaction.user.id and m.channel.id == interaction.channel.id

        await interaction.response.send_message("Reply to this message to add a comment to the profile")
        try:
            comment = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await interaction.followup.send("You didn't reply in time", ephemeral=True)
        else:
            async with aiosqlite.connect('comments.db') as conn:
                async with conn.cursor() as cursor:
                    if len(comment.content) > 50:
                        await interaction.followup.send("Your comment is too long (must be less than 50 characters)", ephemeral=True)
                        return
                        
                    await cursor.execute("INSERT INTO COMMENTS (user, sender_username, comment, date_sent) VALUES (?, ?, ?, ?)", (self.user_id, interaction.user.name, comment.content, datetime.datetime.now()))
                    await conn.commit()

            await interaction.followup.send("Comment added")

class profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.user_message_count = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        user = str(message.author.id)
        if user not in self.user_message_count:
            self.user_message_count[user] = 0
        self.user_message_count[user] += 1

        if self.user_message_count[user] % 5 == 0:
            async with aiosqlite.connect('hamood.db') as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute("SELECT xp, level FROM hamood WHERE user = ?", (user,))
                    result = await cursor.fetchone()
                    if result is None:
                        await cursor.execute("INSERT INTO hamood (user, xp, level) VALUES (?, ?, ?)", (user, 1, 1))
                    else:
                        xp, level = result
                        xp += 1
                        next_level_xp = 100 + (level - 1) * 10
                        if xp >= next_level_xp:
                            xp -= next_level_xp
                            level += 1
                        await cursor.execute("UPDATE hamood SET xp = ?, level = ? WHERE user = ?", (xp, level, user))
                    await conn.commit()

    @slash_command(name='profile', description="Shows a user's profile")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def profile(self, ctx, user: discord.Member):
        print(f"command executed by {ctx.author.name}#{ctx.author.discriminator}")
        async with aiosqlite.connect('hamood.db') as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT reputation, xp, level FROM hamood WHERE user = ?", (str(user.id),))
                result = await cursor.fetchone()
                reputation = result[0] if result else 0
                if result is None:
                    no_xp_embed = discord.Embed(
                        title="This user has 0 XP",
                        color=embed_color
                    )
                    await ctx.respond(embed=no_xp_embed)
                else:
                    reputation, xp, level = result
                    next_level_xp = 100 + (level - 1) * 10
                    profile_embed = discord.Embed(
                        title="User Profile",
                        color=embed_color
                    )
                    profile_embed.add_field(name="Username", value=f"{user.name}")
                    profile_embed.add_field(name="XP", value=f"{xp}/{next_level_xp}")
                    profile_embed.add_field(name="Level", value=f"{level}")
                    profile_embed.add_field(name="Reputation", value=reputation, inline=False)
                    profile_embed.set_thumbnail(url=embed_thumbnail)
                    view = ReputationView(self.bot, user.id)
                    await ctx.respond(embed=profile_embed, view=view)
def setup(bot):
    bot.add_cog(profile(bot))


