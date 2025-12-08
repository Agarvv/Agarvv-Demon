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
    


client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)


    try:
        check_schedule.start()
        print("✅ Task iniciada")
    except Exception as e:
        print(f"❌ Error iniciando task: {e}")
    
@bot.event 
async def on_message(msg):
    print(msg);

keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)