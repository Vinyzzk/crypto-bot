import discord
from discord.ext import commands, tasks
import random

class Talks(commands.Cog):
    """ Works with cryptocurrencies """

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('teste')
        self.gerin_calls.start()

    @tasks.loop(minutes=30)
    async def gerin_calls(self):
        channel = self.client.get_channel(901965451742027838)
        lista = ['Call do rogério? :cold_face: ', ':rocket: <:pvu:905546765330182194> PVU é lua :new_moon: :clown: :rofl:']
        nr = random.randint(1,6)
        if nr == 6:
            await channel.send(random.choice(lista))

def setup(client):
    client.add_cog(Talks(client))
