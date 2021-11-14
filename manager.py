from discord.ext import commands
import random

class Manager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Online")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if 'caralsssho' in message.content:
            await message.channel.send(f'Por favor, {message.author.name}, não ofenda os demais usuários.')
            await message.delete()

        if 'pvu' in message.content:
            nr = random.randint(1,3)
            if nr == 3:
                await message.channel.send(':rocket: PVU é lua :rofl: :clown:')

        await self.client.process_commands(message)

def setup(client):
    client.add_cog(Manager(client))
