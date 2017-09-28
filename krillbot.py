import discord
import asyncio
import requests


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


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
        #Google I'm Feeling Lucky response based on input
        message_content = (str(message.content)).split()[1:]
        if message_content != []:
                url = "http://www.google.com/search?q={}&btnI".format('+'.join(message_content))
                response = requests.get(url)
                while response.url == url:
                    reponse = requests.get(url)
                await client.send_message(message.channel, response.url)
                
                
with open('token.txt', 'r') as myfile:
    client_token = myfile.read()
client.run(client_token)
client.close()