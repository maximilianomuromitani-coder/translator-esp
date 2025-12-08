import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

# Base de datos simple en memoria (puedes cambiarlo a JSON después)
memes = {
    "animales": [
        "https://i.imgflip.com/1bij.jpg",
        "https://i.imgflip.com/26am.jpg",
        "https://i.imgflip.com/7kz3bm.jpg"
    ]
}

@bot.command()
async def animales(ctx):
    """Devuelve un meme aleatorio de animales"""
    meme = random.choice(memes["animales"])
    await ctx.send(meme)

bot.run("TU_TOKEN_AQUI")
