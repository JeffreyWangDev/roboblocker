from backend import *
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3 as sl
from backend import *
from typing import Literal
import os
from dotenv import load_dotenv
import datetime
load_dotenv()
from discord import Interaction
from discord.app_commands import AppCommandError
cogs = [
    "cogs.admin",
    "cogs.panel",
    "cogs.errors"
]

class client(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents,command_prefix=".")
        #self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        for cog in cogs:
            await bot.load_extension(cog)

intents = discord.Intents.default()


bot = client(intents=intents)
# = commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} and ready to roll')
    print('------')



@bot.command()
async def sync(ctx):
    if ctx.author.id == 650431108370137088:
        await ctx.bot.tree.sync(guild=discord.Object(id=919047940843143198))
        await ctx.send(f"Synced!")

@bot.event
async def on_command_error(ctx, error):
    pass
tree = bot.tree

@tree.error
async def on_app_command_error(interaction: Interaction,error: AppCommandError):
    pass

bot.run(os.getenv('discord_token'))