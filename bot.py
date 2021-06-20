import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("ml.hello"):
        await message.channel.send("Hello!!!")
    
client.run(os.getenv('TOKEN'))
