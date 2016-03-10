import discord
import requests
import subprocess
import os
import asyncio

inEmail = input("email: ")
inPassword = input("password: ")

if os.name == "posix":
    os.system("clear")
elif os.name == "nt":
    os.system("cls")


client = discord.Client()

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        if message.content.startswith("!game "):
            input_ = message.content
            input_.split(" ")[0]
            stuff = input_.split(" ")[1:]
            gameName = (" ".join(stuff))
            game = discord.Game()
            game.name = gameName
            await client.change_status(game=game)
            await client.send_message(message.channel, client.user.name + "'s game has been set to " + gameName)
            print("game has been set to" + gameName)
        if message.content.startswith("!exit"):
            await client.logout()

client.run(inEmail, inPassword)
