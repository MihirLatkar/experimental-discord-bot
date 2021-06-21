import discord
import os
import requests
import json
import datetime


client = discord.Client()

def get_data(pin_code):
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    data = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin_code}&date={NextDay_Date}")
    json_data = json.loads(data.text)
    

 

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("ml.hello"):
        await message.channel.send("Hello!!!")
    if message.content.startswith("ml.help"):
        await message.channel.send("Welcome. \n ml.hello - for saying hello \n ml.play <Link> - to play songs \n ml.cowin <pin_code> - to see all slots in your area")
    
client.run(os.getenv('TOKEN'))
