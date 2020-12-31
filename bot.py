import os
from web_scrape import *
from dates import *

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

image = open('image.png', 'rb')
pfp = image.read()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.user.edit(avatar=pfp)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '?dates':
        reset_page_count()
        await message.channel.send(current_page())
    elif message.content == '?dates-next':
        next_page()
        await message.channel.send(current_page())
    elif message.content == '?dates-prev':
        prev_page()
        await message.channel.send(current_page())
    elif message.content == '?nearest':
        await message.channel.send(format_nearest(find_nearest(str_to_dt(formatted('https://uwaterloo.ca/registrar/important-dates/list?academic_year=229&date=All&page=1')))))
    elif message.content == '?help':
        await message.channel.send(helpme())
        
client.run(TOKEN)
