import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged on as {client.user}')


@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
