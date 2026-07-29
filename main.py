import discord
from discord.ext import commands, tasks
from discord import app_commands
import logging
import os
from dotenv import load_dotenv
from flask import Flask
from datetime import datetime, timezone
from threading import Thread
import asyncio
import re

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

saludo = ""

app = Flask('')

@app.route('/')
def home():
    return "OK"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

async def abort(s_param):
    channel = bot.get_channel(890963484181954610)
    await channel.send(f"Aborte a mi pene por error en: {s_param}")
    while True:
        await asyncio.sleep(3600)

spam_channel = None
general_channel = None
s = 0

@bot.tree.command(name="saludo_bienvenida", description="Cambia el saludo q el bot de mierda hara :v")
@app_commands.describe(saludo_param="Nuevo Saludo de Agarv demon")
async def cambiar_saludo(interaction: discord.Interaction, saludo_param: str):
    global saludo
    saludo = saludo_param
    await interaction.response.send_message(f"Saludo actualizado a: {saludo}", ephemeral=True)

async def cambiar_saludo(interaction: discord.Interaction, saludo_param: str):
    global saludo
    saludo = saludo_param
    await interaction.response.send_message(f"Saludo actualizado a: {saludo}", ephemeral=True)

async def cambiar_saludo(interaction: discord.Interaction, saludo_param: str):
    global saludo
    saludo = saludo_param
    await interaction.response.send_message(f"saludo de los cojoncillos actualizado a: {saludo}", ephemeral=True)

# 67
@bot.event
async def on_ready():
    global general_channel, spam_channel
    general_channel = bot.get_channel(997124912475021462)
    spam_channel = bot.get_channel(890963484181954610)
    await bot.tree.sync()

    if general_channel:
        await general_channel.send("hola darle un besito en la frente al hijito de agarvv porfa ñiñiñiñiñiiiii :heart_eyes_cat: ")
    else:
        print("not general channel")

@bot.event
async def on_member_join(member):
    print("pofkjdja")
    
    if saludo == "":
        await general_channel.send(
            f"Bienvenidx {member.mention}! ♡\n"
            "◜ ͡ ◝ Gracias por unirte a nuestra comunidad 𐚁̸\n"
            "Lee las normas y Verifícate  𓎟𓎟 　ৎ ݂ ݁\n"
            "◟ ͜ ◞ El staff está para ayudarte."
        )
    else:
        await general_channel.send(
            f"{member.mention}\n"
            f"{saludo}"
        )

@bot.event
async def on_message(msg):
    
    replace = "aeouáéóúAEOUÁÉÓÚ"

    if message.author.bot:
        
        return

    if msg.channel.id == 890963484181954610:
        
        send = ""

    for c in msg.content:
        
        if c in replace:
            
            send += "i" if c.islower() else "I"
        else:
            send += c

    await msg.reply(send)
     
                
        

    match msg.content:
        case "ACK":
            if s == 0:
                await msg.channel.send("SYN-ACK")
                s = 1
            else:
                await msg.channel.send("ACK")
                s = 0
        case "2025?":
            await msg.channel.send("FELIZ 2026 AAAAAAAAAAAA")

    match_obj = re.match(r'^pegale a (.+)$', msg.content, re.IGNORECASE)
    if match_obj:
        username = match_obj.group(1)
        protected = ("agarv", "agarvv", "agar", "garv")
        if username.lower() in protected:
            await msg.channel.send("ño ño ñooo a papi no le pego >w<")
            return
        await msg.channel.send(f"Pum pum {username} serda guarrindonga mala uwu")

keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
