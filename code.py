import os
from tabnanny import process_tokens
import discord
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
load_dotenv()
TOKEN = os.getenv('OTk0MTkxMjI1MTQzOTU5NjU0.G1AGAh.xaworGgwVCm4FfUjNWhjjajpB8XVmJoAe6cizQ')

