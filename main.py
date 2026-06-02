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
    
@bot.event
async def on_ready():
    guild = bot.guilds[0]
    start = datetime(2026, 5, 1)
    end = datetime(2026, 5, 31, 23, 59, 59)
    r = 0
    saved = []
    channel = bot.get_channel(890963484181954610);
    await channel.send("<&1183086057344991263> no soy un monstruo gorda puta. yo no abortare a mis hijos como tu abortaste a tado, osea... panza, panza, panza, panza. mileurista, mileurista, mileurista. es como.. fuck. yo no puedo aguantar mucho mas aqui, ¿sabes?")
    print("hola")
        
    
    try:  
        for channel in guild.text_channels:
            try: 
                async for message in channel.history(after=start, before=end, limit=None):
                    print(message.created_at)
                    if message.author.id not in saved:
                        saved.append(message.author.id)

                    if r >= 1000:
                        r = 0
                        await asyncio.sleep(1)
                        
                    else:
                        r += 1

            except Exception as e:
                print(f"error3: {type(e).__name__} - {str(e)}")  
                await channel.send("error de no seq nosecuanto0")
                while(1 > 0): 
                    await asyncio.sleep(3600)

    except:
        print(f"error3: {type(e).__name__} - {str(e)}")  
        print("error3")
        await channel.send("error de no seq nosecuanto")
        while(1 > 0): 
            await asyncio.sleep(3600)
    
    print("pollaaaaaa")
    async for idd in saved:
        user = await guild.get_member(idd) 
        
        printf(f"user: {user.username}")
        
    await channel.send(f"Se libraron {len(saved)} usuarios, sidiikslxcskl")
    while(1 > 0): 
        await asyncio.sleep(3600)


    async for member in guild.fetch_members(limit=None):
        if member.id not in saved and not member.bot:  
            try:
                await member.kick(reason="kick por inactivo.......... :v")
                await asyncio.sleep(0.5)  
            except:
                abort("kick")
            
            
            
        
        


    try:
        check_schedule.start()
        print("✅ Task iniciada")
    except Exception as e:
        print(f"❌ Error iniciando task: {e}")

spam_channel = bot.get_channel(890963484181954610) 
s = 0 

@bot.event
async def on_message(msg):
    if msg.author.bot or msg.channel.id != 890963484181954610:
        return
    
    res = model.predict(msg.content) 
    await msg.channel.send(res); 
    global s

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