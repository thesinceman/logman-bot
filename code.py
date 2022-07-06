import discord

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

client.run('OTk0MTkxMjI1MTQzOTU5NjU0.GU8vBj.Q5-oYi9j7DOvHZjqZRG3_T7DMLfIWz26R8FfDM')
