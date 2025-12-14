# Bot con imágenes aleatorias y TODAS las funciones originales
import discord
from discord.ext import commands
import random

# -----------------------------
# Generador de contraseñas
# -----------------------------
def gen_pass(length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(length))

# -----------------------------
# Intents necesarios
# -----------------------------
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

# -----------------------------
# Evento ON_READY
# -----------------------------
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# -----------------------------
# TODOS TUS COMANDOS ORIGINALES
# -----------------------------
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def password(ctx, length: int = 8):
    await ctx.send(f"Tu contraseña es: {gen_pass(length)}")

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

# ---------------------------------------------------
# 🔥 LISTA DE IMÁGENES (todas con nombre imagenesX)
# ---------------------------------------------------
imagenes_random = [
    "imagenes/imagenes1.jpg",
    "imagenes/imagenes2.jpg",
    "imagenes/imagenes3.jpg",
    "imagenes/imagenes4.jpg"
]

# ---------------------------------------------------
# 🔥 COMANDO ?meme FUNCIONAL AL 100%
# ---------------------------------------------------
@bot.command()
async def meme(ctx):
    await ctx.send("🔍 Generando meme...")

    try:
        imagen = random.choice(imagenes_random)
        file = discord.File(imagen)
        await ctx.send(file=file)

    except Exception as e:
        await ctx.send(f"❌ Error al enviar imagen: {e}")
        await ctx.send("Revisa que la carpeta **imagenes/** tenga los archivos imagenes1.jpg, imagenes2.jpg, etc.")

# ---------------------------------------------------
# 🔍 Comando para verificar qué imágenes detecta
# ---------------------------------------------------
@bot.command()
async def debug_meme(ctx):
    import os

    if not os.path.exists("imagenes"):
        await ctx.send("❌ La carpeta 'imagenes' NO existe.")
        return

    archivos = os.listdir("imagenes")
    await ctx.send(f"📂 Archivos encontrados: {archivos}")

# -----------------------------
# Token del bot
# -----------------------------
bot.run("your token")
