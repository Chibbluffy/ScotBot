# scotbot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('SCOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    dm_content = ''

    if reaction.emoji == '🏁':
        for react in reaction.message.reactions:
            if react.emoji == '🏁':
                continue
            dm_content += str(react.emoji) + '\n'
            users_with_this_react = await react.users().flatten()

            for u in users_with_this_react:
                dm_content += u.display_name + '\n'

            if not user.dm_channel:
                await user.create_dm()
            await user.dm_channel.send(content=dm_content)

client.run(TOKEN)
