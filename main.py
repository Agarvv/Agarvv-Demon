import discord 
from discord.ext import commands
import logging 
import os 
from dotenv import load_dotenv 
from flask import Flask
from threading import Thread

load_dotenv() 
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf8', mode='w')

intents = discord.Intents.default()
intents.message_content = True 
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
    print("Bot running!")


keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)