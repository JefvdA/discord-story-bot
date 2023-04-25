import discord.ext.commands

from story_bot.cogs.ping_cog import PingCog


async def add_cogs(bot: discord.ext.commands.Bot):
    print(f'Adding cogs...')
    await bot.add_cog(PingCog(bot))
    print(f'Cogs added!')
