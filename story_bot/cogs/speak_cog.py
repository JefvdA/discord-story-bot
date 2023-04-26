import discord
from discord import app_commands
from discord.ext import commands


class SpeakCog(commands.Cog):
    def __init__(self, bot: discord.ext.commands.Bot):
        self.bot = bot

    @app_commands.command()
    async def speak(self, interaction: discord.Interaction):
        voice_channel_id = interaction.user.voice.channel.id
        voice_channel = await self.bot.fetch_channel(voice_channel_id)
        if isinstance(voice_channel, discord.VoiceChannel):
            await voice_channel.connect()
        await interaction.response.send_message(f'Hi {interaction.user.display_name}, I have joined your voice channel!')
