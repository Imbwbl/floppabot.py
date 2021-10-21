import discord
import os
import json
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True #Intents important !
bot = commands.Bot("!", intents = intents) # Défini le bot

bot.remove_command("help")



# Charge les commandes du fichier cogs

@bot.event
async def on_ready():
    print(f'Connecté à {bot.user}')
    print(discord.__version__)
    print(os.system("python -V"))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"?help"))

@bot.command()
async def floppa(ctx):
    chiffre = random.randint(1,204)
    await ctx.send(f"https://bigfloppa.net/gallery/images/floppa{chiffre}.jpg")

# ------------------------ Lancement du bot ------------------------ # 
with open("config.json", "r") as config:
    data = json.load(config)
    token = data["token"]
bot.run(token) 
