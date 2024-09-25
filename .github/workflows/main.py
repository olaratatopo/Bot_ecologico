import discord
import requests
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command("mazetas_plastico")
async def mazetas_de_plastico (ctx):
    await ctx.send("Se puede utilizar las botellas de plastico para crear mazetas haciendo agujeros para las plantas y para que salga el agua reduciendo el plastico y haciendo vida, para un ejemplo escribe $mazeta")
@bot.command("botella_lapices")
async def botella_lapices (ctx):
    await ctx.send("Se pueden crear portalapices con una botella chica cortando la parte de arriba y se pueden pintar para que se vea mejor, para un ejemplo escribe $portalapices")
@bot.command("abaco_tapas")
async def abaco_tapas (ctx):
    await ctx.send("Se puede crear un abaco reutilizando tapitas alambre y un pedazo de madera, para un ejemplo escribe $abaco")
@bot.command("botella_alimentos")
async def botella_para_guardar_alimentos (ctx):
    await ctx.send("Cortando la tapa de abajo de dos botellas y uniendolas se pueden hacer ecipientes para guardar comida duradera como arroz, para un ejmplo escribe $botella_comida")

@bot.command()
async def mazeta (ctx):
    with open(f"bot_ecologico/images/mazetas_plastico.jpg", "rb") as f:
            picture = discord.File(f)  
    await ctx.send(file=picture)
@bot.command()
async def portalapices (ctx):
    with open(f"bot_ecologico/images/botellas_para_lapizes.jpg", "rb") as f:
            picture = discord.File(f)  
    await ctx.send(file=picture)
@bot.command()
async def abaco (ctx):
    with open(f"bot_ecologico/images/abaco_tapitas.jpg", "rb") as f:
            picture = discord.File(f)  
    await ctx.send(file=picture)
@bot.command()
async def botella_comida (ctx):
    with open(f"bot_ecologico/images/botellas_para_guardar.jpg", "rb") as f:
            picture = discord.File(f)  
    await ctx.send(file=picture)
@bot.command()
async def ayuda (ctx):
     await ctx.send("PAra saber informacion escribe ,$mazetas_plastico,$botella_lapices,$abaco_tapas,$botella_alimentos")
bot.run("MTI4NjEwNzQxMjYwODE4ODQ2Ng.GDRUzP.oWJdEDSk2XHT2g0ccMqz4fFiorIB1EvNJACEWc")
