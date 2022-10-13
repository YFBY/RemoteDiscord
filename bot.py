#discord bot for stuff?
#imports
import discord
from discord.ext import commands 
import socket
import easyserver
import json #use to load data and save data and config

#discord output

with open("config.json") as cf:
	ConfigFile = json.load(cf)

ServerManager = easyserver.server()

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())

token = ConfigFile.get("Discord").get("Token")

serverchanneli = ConfigFile.get("Discord").get("InputChannel")
serverchannelo = ConfigFile.get("Discord").get("OutputChannel")

channeli = None
channelo = None



@client.event
async def on_ready(): #the SEND IF READY
	global channeli, channelo

	print(f"running as user: {client.user}")

	channeli = client.get_channel(serverchanneli)

	channelo = client.get_channel(serverchannelo)

	await channelo.send("```Server Bot Ready```")


@client.command()
async def ip(ctx):
	await channelo.send(f"current ip: ```{ServerManager.ip()}```")


@client.command()
async def server(ctx, *msg):
	if msg[0] == "start":
		await channelo.send(f"```{ServerManager.start(msg[1])}```")

	elif msg[0] == "state":
		await channelo.send(f"Process State: ```{ServerManager.state()}```")


	elif msg[0] == "output":
		await channelo.send(f"```{ServerManager.output()}```")
 
	elif msg[0] == "input":
		ServerManager.input(' '.join(msg[1:]) + '\n')


if __name__ == "__main__": #MAIN
	client.run(token)
