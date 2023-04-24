import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')


@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
