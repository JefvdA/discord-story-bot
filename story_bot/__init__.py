import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)
tree = bot.tree


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')
    sync_commands_result = await bot.tree.sync()
    print(f'Synced {len(sync_commands_result)} slash commands.')


@tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('pong')
