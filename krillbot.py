import discord
import asyncio
import aiohttp


client = discord.Client()
krill_player = None
class player_obj:
    def __init__(self, channel_to_join):
        self.channel_to_join = channel_to_join
    async def print_message(self):
        print("Hello")
    async def join_server(self):
        voice_channel = await client.join_voice_channel(self.channel_to_join)
        player = await voice_channel.create_ytdl_player('https://www.youtube.com/watch?v=3mUfOs-CTCw')
        player.volume = 0.5
        player.start()
        print("Joined voice channel {}".format(channel))
    async def print_server(self):
        print(player)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for server in client.servers:
        for channel in server.channels:
            if str(channel.type) == "voice":
                if not discord.opus.is_loaded():
                    discord.opus.load_opus('/usr/local/lib/libopus.so')
                global krill_player 
                krill_player = player_obj(channel)
                await krill_player.print_message()
                await krill_player.join_server()
                await krill_player.print_server()

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
        return response.url

#Token and running bot stuff
with open('token.txt', 'r') as myfile:
    client_token = myfile.read()
client.run(client_token)
client.close()
    