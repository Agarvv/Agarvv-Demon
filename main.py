import discord 
from discord.ext import commands, tasks
import logging 
import os 
from dotenv import load_dotenv 
from flask import Flask
from datetime import datetime, timezone
from threading import Thread
import asyncio
import openai 
from openai import OpenAI


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


@bot.event
async def on_ready():
    


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
            
        case "pegale a tado":
            await msg.channel.send("pum pum tado malo uwu")
            
        case "quote":
            await msg.channel.send("<@949479338275913799>") 
            
 

keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)