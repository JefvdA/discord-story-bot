import discord
from discord.ext import commands
from story_bot.cogs.ping_cog import PingCog

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')

    print(f'Adding cogs...')
    await bot.add_cog(PingCog(bot))

    print(f'Syncing commands')
    sync_commands_result = await bot.tree.sync()
    print(f'Synced {len(sync_commands_result)} slash commands.')
