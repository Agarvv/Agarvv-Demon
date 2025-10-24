import discord 
from discord.ext import commands
import logging 
import os 


from dotenv import load_dotenv 

load_dotenv() 

token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf8', mode='w')
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='/', intents=intents) 


@bot.event
async def on_ready():
    print("Runs")
    
bot.run(token, log_handler=handler, log_level=logging.DEBUG)