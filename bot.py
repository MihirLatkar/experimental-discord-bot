import discord
import os
import requests
import json
import datetime


client = discord.Client()


day = str(datetime.datetime.today().day+1)
month = str(datetime.datetime.today().month)
year = str(datetime.datetime.today().year)
date = day + "-" + month + "-" + year


def get_data(pin_code):
    Vaccines = ["Name  |  Address  |  total available  |  available for dose 1  |  available for dose 2  |  min age limit  | Vaccine"]
    url = (
        f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin_code}&date={date}")
    # print(f"{url=}")
    data = requests.get(url)
    json_data = json.loads(data.text).get("sessions")

    # print(json_data)
    if json_data == None:
        return []
    for i in range(len(json_data)):
        Vaccines.append(json_data[i]["name"] + "  |  " + json_data[i]["address"] + "  |  " + str(json_data[i]["available_capacity"]) + "  |  " + str(json_data[i]
                        ["available_capacity_dose1"]) + "  |  " + str(json_data[i]["available_capacity_dose2"]) + "  |  " + str(json_data[i]["min_age_limit"]) + "  |  " + json_data[i]["vaccine"])
    
    return Vaccines


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
        await message.channel.send("Welcome. \n ml.hello - for saying hello \n ml.cowin <pin_code> - to see all slots in your area")
    if message.content.startswith("ml.cowin"):
        check = message.content.split()
        if len(check) == 2:
            pin = check[1]
            if len(pin) == 6:
                Vaccines = get_data(pin)
                if not Vaccines:
                    await message.channel.send(f"Invalid Pin number")
                if len(Vaccines) == 1:
                    await message.channel.send(f"No Slots available in {pin} :cry:")
                    return 
                for i in range(len(Vaccines)):
                    await message.channel.send(Vaccines[i])
            else:
                await message.channel.send(f"Invalid Pin number")
        else:
            await message.channel.send("ml.cowin <pin_code> - to see all slots in your area")


client.run(os.getenv('TOKEN'))