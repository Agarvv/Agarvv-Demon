import discord 
from discord.ext import commands, tasks
import logging 
import os 
from dotenv import load_dotenv 
from flask import Flask
from datetime import datetime, timezone
from threading import Thread
import asyncio

welcome_channel = 1431704967760183448


async def is_from_today_message(message):
    # message date may appear
    # in the following format:
    # 2025-10-25 18:09:28.128000+00:00.

    # We are required to extract
    # the year, month, and day 
    # from this format and verify if
    # they correspond to 
    # the current day, year, and month.
    
    
    date = message.created_at
    now = datetime.now() 
    
    if date.year == now.year and date.month == now.month and date.day == now.day:
        return True 
    
    return False 














async def get_members_by_date(date, guild: discord.Guild):

    members = []

    target_date = date.astimezone(timezone.utc).date()


    async for member in guild.fetch_members(limit=None):
        
        if member.joined_at is None:
            print("debug")
            continue
        
        joined_date = member.joined_at.astimezone(timezone.utc).date()
        
        if joined_date == target_date:
            members.append(member)

    return len(members)







async def get_average_joins(guild: discord.Guild):
    # retrieve all members,
    # filter them by join date day, 
    # and then calculate the average number
    # of user joins. Since this average can 
    # fluctuate significantly,
    # it will require continuous updates.
    members = []
    
    async for member in guild.fetch_members(limit=None):
        members.append(member)
    
    return members






def get_users_joined_today():
    return []

users_joined_today = get_users_joined_today()
average_joins_per_day = 0 

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




async def check_anomalies():
    # get users that joined today 
    pass 
        

@tasks.loop(seconds=60)  
async def check_schedule():
    now = datetime.now()
    if now.hour == 0 and now.minute == 0:  
        await check_anomalies()
        await asyncio.sleep(61)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        users = await get_average_joins(guild)
        for user in users:
            print(user.joined_at)
    
    print("Bot running!")
    check_schedule.start()

keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)