import discord 
from discord.ext import commands,tasks
import asyncio
import os
from keep_alive import keep_alive
import youtube_dl
from dotenv import load_dotenv


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
  

    """
  if message.content.is('ufo'):
    await message.channel.send('DU WAGST ES UNS ZU ERWÄHNEN???')

  if message.content.is('UFO'):
    await message.channel.send('DU WAGST ES UNS ZU ERWÄHNEN???')
  
  """
  if message.content.startswith('?ufo help'):
    embed = discord.Embed(title='UFO BOT',
    description = 'all comands -- prefix is   ?ufo \r\n',
    color=0x9AFF0A,)

    
    embed.add_field(name='?ufo help', value='shows this help page', inline = False)
    embed.add_field(name='?ufo future', value='predicts the future', inline = False)
    embed.add_field(name='?ufo status', value='shows current bot status', inline = False)

    embed.set_footer(text='You dont have to find out more about us...')

    await message.channel.send(embed=embed)


  if message.content.startswith('?ufo status'):
    await message.channel.send('collecting information about humans...  ')
    await message.channel.send('https://cdn.dribbble.com/users/59100/screenshots/1869567/ufo.gif')

  if message.content.startswith('?ufo future'):
    await message.channel.send('WE WILL RULE THE WORLD')

  if message.content.startswith('?ufo info'):
    await message.channel.send('These information we have collected about you:')


keep_alive()
client.run(os.getenv('TOKEN'))