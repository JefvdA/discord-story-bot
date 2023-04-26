import discord.ext.commands

from story_bot.cogs.ping_cog import PingCog
from story_bot.cogs.speak_cog import SpeakCog


async def add_cogs(bot: discord.ext.commands.Bot):
    print(f'Adding cogs...')
    await bot.add_cog(PingCog(bot))
    await bot.add_cog(SpeakCog(bot))
    print(f'Cogs added!')
