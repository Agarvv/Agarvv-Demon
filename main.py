import discord 
from discord.ext import commands, tasks
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




app = Flask('')

@app.route('/')
def home():
    return "OK"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

async def abort(s):
    channel = bot.get_channel(890963484181954610);
    await channel.send(f"Aborte a mi pene por error en: {s}")
    while(1 > 0):
        await asyncio.sleep(3600)

spam_channel = bot.get_channel(890963484181954610) 
general_channel = bot.get_channel(997124912475021462)
s = 0 
    
general_channel = None  # Definir como None globalmente

@bot.event
async def on_ready():
    global general_channel, spam_channel 
    general_channel = bot.get_channel(997124912475021462)
    spam_channel = bot.get_channel(890963484181954610)
    
    
    if general_channel:
        await general_channel.send("ya me canse de esta vida cruel papi matame")
    else:
        print("not general channel")




import discord

@bot.event
async def on_member_join(member):
        await general_channel.send(f"¡Bienvenidx {member.mention} al servidor, pasala de puta madre y no olvides beber agua y nunca tomar acido sulfurico bajo ningun concepto, y que karlita te acompanie en todas tus acciones. (saludenlx todos, o os cojo.)")

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    
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