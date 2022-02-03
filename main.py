# Bot do discord da taverna
# Autor: Gabriel de Nazaré / SUPerchokki

# Importando a biblioteca do discord
import discord

# Importando o configurador de comandos
from discord.ext import commands

# Criando o client(usuario) do discord
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith('oi'):
        if str(message.author) == "marechal#3177":
            await message.channel.send("Ola")
        elif str(message.author) == "SUPerchokki#4524":
            await message.channel.send("Nhain Gabs")
        elif str(message.author) == "SH4Z4N#0215":
            await message.channel.send("Fala corno")
        else:
            await message.channel.send("nhain " + str(message.author) + "!")

    if message.content.startswith('$help'):
        await message.channel.send('n tem outro comando')

with open('TOKEN.txt', 'r') as f:
    token = f.read()

client.run(token)
