import discord
import os
import random
from discord.ext import commands

img_names = ['mem1.jpg', 'mem2.jpg', 'mem3.jpg']

intents = discord.Intents.default()
intents.message_content = True

# Elimina el prefijo por completo
bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    # Obtiene el nombre del usuario que envió el mensaje
    author_name = ctx.author.display_name
    # Responde con un saludo y el nombre del usuario
    await ctx.send(f'Hola, {author_name}!')

@bot.command(name='mem')
async def mem(ctx):
    # Selecciona aleatoriamente una imagen de la lista img_names
    selected_image = random.choice(img_names)

    # Construye la ruta completa al archivo de la imagen
    img_path = os.path.join('images', selected_image)

    # Verifica si el archivo existe
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send("La imagen no fue encontrada.")

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'bienvenido {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)


bot.run('') #aqui va el TOKEN
