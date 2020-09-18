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
    if reaction.emoji == '🏁':
        for react in reaction.message.reactions:
            if react.emoji == '🇾':
                yreaction = react
            print(react)

        yes_men = await yreaction.users().flatten()
        result = []

        for man in yes_men:
            result.append(man.display_name)
        if not user.dm_channel:
            await user.create_dm()
        await user.dm_channel.send(content=', '.join(result))

client.run(TOKEN)
