import discord
import asyncio
import aiohttp


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#Main event for controlling all actions on message
@client.event
async def on_message(message):
    if message.content == '`exit':
        #Exit if user is SupineKrill#9842, otherwise alert
        if str(message.author) == "SupineKrill#9842":
            await client.send_message(message.channel, 'Exiting...')
            await client.close()
        else:
            await client.send_message(message.channel, "Only available for SupineKrill")
    elif message.content[:7] == "`google":
        #Return I'm feeling lucky result from google
        message_content = (str(message.content)).split()[1:]
        if message_content != []:
            url = await return_url("http://www.google.com/search?q={}&btnI".format('+'.join(message_content)))
            await client.send_message(message.channel, url)

async def return_url(url):
    async with aiohttp.request('GET', url) as response:
        print(response.headers)
        return response.url

#Token and running bot stuff
with open('token.txt', 'r') as myfile:
    client_token = myfile.read()
client.run(client_token)
client.close()
    