import discord
import requests
import subprocess


inEmail = input("email: ")
inPassword = input("password: ")


client = discord.Client()
client.login(inEmail, inPassword)
@client.event
def on_message(message):
    if message.author.id == client.user.id:
        if message.content.startswith("!game "):
            input_ = message.content
            input_.split(" ")[0]
            stuff = input_.split(" ")[1:]
            gameName = (" ".join(stuff))
            game = discord.Game()
            game.name = gameName
            client.change_status(game=game)
            client.send_message(message.channel, client.user.name + "'s game has been set to " + gameName)
            print("game has been set to" + gameName)

client.run()
