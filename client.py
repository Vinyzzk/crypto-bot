from discord.ext import commands
import os

client = commands.Bot('$')

def load_cogs(client):
    for file in os.listdir('tasks'): 
        if file.endswith(".py"):
            cog = file[:-3]
            client.load_extension(f"tasks.{cog}")

    for file in os.listdir('commands'):
        if file.endswith(".py"):
            cog = file[:-3]
            client.load_extension(f"commands.{cog}")

load_cogs(client)

client.run(' maskared token =p ')