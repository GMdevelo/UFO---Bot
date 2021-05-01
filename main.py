import discord 
import asyncio
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  client.loop.create_task(status_task())

async def status_task():
  while True:
      await client.change_presence(activity=discord.Game('spying on humans'), status=discord.Status.online)
      await asyncio.sleep(10)
      await client.change_presence(activity=discord.Game('killing humans'), status=discord.Status.online)
      await asyncio.sleep(3)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('?ufo future'):
    await message.channel.send('WE WILL RULE THE WORLD')

  if message.content.startswith('?ufo help'):
    embed: discord.Embed(title='UFO BOT')
    await message.channel.send('**UFO BOT**\r\n ```?ufo help -- zeigt diese Hilfe```')

keep_alive()
client.run(os.getenv('TOKEN'))