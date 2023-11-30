import discord
import os 
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv() 
bot = discord.Bot(help_command=None)

intents = discord.Intents.all()
intents=intents

for fn in os.listdir("./Cogs/Commands/Animal"): 
    if fn.endswith(".py"):
        bot.load_extension(f"Cogs.Commands.Animal.{fn[: -3]}")

for fn in os.listdir("./Cogs/Commands/Economy"): 
    if fn.endswith(".py"):
        bot.load_extension(f"Cogs.Commands.Economy.{fn[: -3]}")

for fn in os.listdir("./Cogs/Commands/Emotes"):
    if fn.endswith(".py"):
        bot.load_extension(f"Cogs.Commands.Emotes.{fn[: -3]}")

for fn in os.listdir("./Cogs/Commands/Fun"):
    if fn.endswith(".py"):
        bot.load_extension(f"Cogs.Commands.Fun.{fn[: -3]}")
        
for fn in os.listdir("./Cogs/Commands/General"):
    if fn.endswith(".py"):
        bot.load_extension(f"Cogs.Commands.General.{fn[: -3]}")

for fn in os.listdir("./Cogs/Commands/Moderation"):
    if fn.endswith(".py"):
        bot.load_extension(f"Cogs.Commands.Moderation.{fn[: -3]}")

for fn in os.listdir("./Cogs/Events"):
    if fn.endswith(".py"):
        bot.load_extension(f"Cogs.Events.{fn[: -3]}")
        
for fn in os.listdir("./Cogs/Commands/Owner"):
    if fn.endswith(".py"):
        bot.load_extension(f"Cogs.Commands.Owner.{fn[: -3]}")

bot.run(os.getenv('TOKEN')) 