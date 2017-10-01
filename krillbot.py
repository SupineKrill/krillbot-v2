import discord
import asyncio
import aiohttp
from discord.ext import commands


client = discord.Client()
krill_player = None


class player_obj:

    def __init__(self, channel_to_join):
        self.channel_to_join = channel_to_join
        self.player_volume = 0.05
        self.player = None
        self.voice_channel = None

    async def play_song(self, song_url):
        try:
            self.player.is_playing()
        except:
            self.voice_channel = await client.join_voice_channel(self.channel_to_join)
            self.player = await self.voice_channel.create_ytdl_player(song_url, after=my_after)
            self.player.volume = player_volume
            self.player.start()

    async def stop_player(self):
        self.player.stop()
        await self.voice_channel.disconnect()
        self.player = None
        self.voice_channel = None
        
    async def set_volume(self, volume_to_set):
        try:
            self.player_volume = float(volume_to_set)
        except:
            await client.send_message(message.channel, 'Enter a float value. (0.0-1.0)')


def my_after():
    krill_player.player.stop()
    coro = krill_player.voice_channel.disconnect()
    fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
    krill_player.player = None
    krill_player.voice_channel = None
    try:
        fut.result()
    except:
        pass


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

# Main event for controlling all actions on message


@client.event
async def on_message(message):
    if message.content == '`exit':
        # Exit if user is SupineKrill#9842, otherwise alert
        if str(message.author) == "SupineKrill#9842":
            await client.send_message(message.channel, 'Exiting...')
            await client.close()
        else:
            await client.send_message(message.channel, "Only available for SupineKrill")
    elif message.content[:7] == "`google":
        # Return I'm feeling lucky result from google
        message_content = (str(message.content)).split()[1:]
        if message_content != []:
            url = await return_url("http://www.google.com/search?q={}&btnI".format('+'.join(message_content)))
            await client.send_message(message.channel, url)
    elif message.content[:8] == "`youtube":
        message_content = (str(message.content)).split()[1:]
        if message_content != []:
            url = await return_url("http://www.google.com/search?q={}+site%3Ayoutube.com&btnI".format('+'.join(message_content)))
            await krill_player.play_song(url)
    elif message.content == "`stop music":
        await krill_player.stop_player()
    elif message.content[:7] == "`volume":
        await krill_player.stop_player(messsage.content[8:11])


async def return_url(url):
    async with aiohttp.request('GET', url) as response:
        return response.url

# Token and running bot stuff
with open('token.txt', 'r') as myfile:
    client_token = myfile.read()
print(client_token)
client.run(client_token)
client.close()
