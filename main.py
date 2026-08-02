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
import random 

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

vacilones = [
    "no se de lo que me hablas primo preguntale a jaz porfa q yo ni idea tengo no me toques los cojones porfavor o me asegurare de que... nada nada. ignoralo............",
    "tio que NO ENTIENDO LO QUE ME CUENTAAAAAAAASSSSS. dejame en paz",
    
    "no te entiendo no me toques mas los cojones del lago nes",
    
    "me duelen los pies dejame en paz porfavor"
    "no tengo ganas de hablar ahora",
    "estoy triste porque agarvv se metio un palo de escoba por el culo y tuvo diarrea radioactiva, dejame rn paZ",
    "no ahora no bro, estoy ocupado jugando con papa",
    "q miras bobo, q miras bobo? anda pa ya bobo anda pa ya",
    "no me hables",
    "NO ME HABLES COÑO",
    "no puedo pensar con claridad para responder ahora mismo, diselo a jaz",
    "ma doare in pula de ce spui, lasa-ma in pace",
        "no c bro no tengo ni idea",
    "preguntale a otra persona q yo hoy no pienso",
    "q dices tio me acabo de despertar",
    "ni idea la vrd",
    "me da muchisima pereza responder ahora",
    "no quiero pensar lo siento",
    "bro no me da el cerebro ahora mismo",
    "no me apetece hablar",
    "hoy estoy en modo npc",
    "preguntale a jaz q seguro sabe algo",
    "de verdad esperabas q lo supiera?",
    "me pillaste en mal momento",
    "no tengo ganas de responder lo siento primo",
    "q va bro ni idea",
    "me supera esa pregunta",
    "no me rayes porfa",
    "ahora mismo no puedo pensar",
    "se me apago el cerebro",
    "tengo la cabeza en otro sitio",
    "espera... no mejor no",
    "no c responder eso",
    "me niego educadamente",
    "no gracias",
    "paso bro",
    "me da una pereza criminal",
    "estoy demasiado cansao pa pensar",
    "esa pregunta viene muy fuerte",
    "ni ganas ni fuerzas",
    "haz como si nunca hubieras preguntado",
    "preguntale a tito",
    "preguntale a daniel",
    "preguntale a hasiel",
    "preguntale a alba",
    "preguntale a anne",
    "preguntale a jaz lonjas mortales",
    "tado seguro improvisa algo",
    "yo no",
    "no quiero meter la pata mejor",
    "si respondo la lio",
    "prefiero quedarme callao",
    "hoy no trabajo",
    "estoy de vacaciones mentales",
    "estoy afk del cerebro",
    "me pillaste sin neuronas",
    "hoy vine sin conocimientos",
    "me deje las respuestas en casa",
    "se me olvido como pensar",
    "ni idea hermano",
    "eso ya es mucho pa mi",
    "bro no soy wikipedia",
    "yo solo existo",
    "me estas pidiendo demasiado",
    "esa pregunta tiene demasiadas letras",
    "me canse de leer en la tercera palabra",
    "me rendi antes de entenderla",
    "uffff q complicado",
    "haz de cuenta q no me viste",
    "no puedo ayudarte ahora mismo",
    "hoy no estoy operativo",
    "reiniciando ganas de responder...",
    "error las ganas no fueron encontradas",
    "no tengo permiso para pensar",
    "mi abogado me recomendo no responder",
    "me da ansiedad contestar eso",
    "me da vergüenza equivocarme",
    "prefiero no decir nada",
    "bro sinceramente ni idea",
    "estoy ocupado respirando",
    "estoy ocupado existiendo",
    "no me pagan suficiente pa responder",
    "si supiera te lo diria",
    "ojala supiera",
    "ni jaz sabe eso creo",
    "hasta agarvv roba cobre sabe mas q yo",
    "agarvv me desconecto las neuronas",
    "tito me dejo sin cerebro",
    "jaz se llevo mis ganas de hablar",
    "daniel seguro responde con confianza aunque no sepa",
    "hasiel me rompio el sistema",
    "anne me silenció",
    "alba me dijo q hoy no respondiera",
    "karlita me dio el dia libre",
    "toy cansao jefe",
    "hoy no toca",
    "mañana tampoco seguramente",
    "me niego con todo el respeto del mundo",
    "ni aunque me pagues",
    "no insistas porfa 😭",
    "haz otra pregunta... no espera tampoco",
    "esa no me la se",
    "esa nunca me la enseñaron",
    "yo vine a mirar",
    "me encontraron en la calle no esperes mucho de mi",
    "soy un bot pero tampoco hago milagros",
    "me falta una actualizacion",
    "todavia estoy cargando",
    "cargando respuesta... 0%",
    "cargando respuesta... error",
    "demasiado trabajo para un domingo",
    "mi ultima neurona renuncio",
    "no encuentro las ganas",
    "no me sale responder",
    "esa pregunta me intimida",
    "voy a fingir q no lei eso",
    "voy a mirar pa otro lado",
    "q miedo responder",
    "mejor preguntale a alguien inteligente",
    "yo claramente no entro en esa categoria",
    
]


questions_r = [
    "zi",
    "no",
    "ñope",
    "siiiiicicici",
    "zi zi zi",
    "sipi",
    "sipirili",
    "sipiruliii",
    "zi señor",
    "zi mi rey",
    "zi mi lord (matenme porfavor me duelen los pies)",
    "zi definitivamente",
    "zi al 1000%",
    "zi pero con lag",
    "zi pero no kiero",
    "zi creo",
    "zi supongo",
    "zi probablemente",
    "zi creo k si",
    "zi confirmado",
    "zi aprobado por la nasa",
    "zi aceptado por el consejo",
    "zi modo dios",
    "zi ultra zi",
    "siii",
    "siiii",
    "siiiiiiii",
    "siiiii pero con miedo",
    "siii claro k zi",
    "sii bro",
    "sii maquina",
    "sii papu",
    "sii xd",
    "sii uwu",
    "sisisisisisi",
    "sisisi",
    "sisoy",
    "seee",
    "seeeh",
    "seeeee",
    "claramente zi",
    "obvio k zi",
    "obio zi",
    "obio k si",
    "clarisimo bro",
    "confirmadisimo",
    "100% zi",
    "200% zi",
    "infinito zi",
    "respuesta positiva.exe",
    "acepto la mision",
    "procedo a decir zi",

    "no",
    "nop",
    "nopi",
    "nope",
    "ño",
    "ñop",
    "ñope",
    "nel",
    "nelson",
    "nel pastel",
    "negativo maquina",
    "negativo bro",
    "ni d broma",
    "ni loco",
    "ni en sueños",
    "no k va",
    "no creo",
    "no se yo eh",
    "no confirmado",
    "rechazado por el consejo",
    "rechazado por la nasa",
    "error 404: si no encontrado",
    "mi respuesta es no.exe",
    "imposible bro",
    "eso no pasa los tests",
    "mi cpu dice no",
    "mi ram dice no",
    "mi gato dice no",
    "mi calculadora dice no",
    "nope nope nope",
    "no no no no",
    "nananai",
    "nanai del paraguai",
    "ni de coña",
    "ni aunque me paguen",
    "paso totalmente",
    "cancelado",
    "rechazado elegantemente",
    "mi voto es no",
    "la ecuacion da no",
    "la fisica dice no",
    "el universo dice no",
    "Schrodinger dice k es no y si a la vez",
    "depende xd",
    "tal vez",
    "quizas",
    "puede ser",
    "50% zi 50% no",
    "mi cerebro esta cargando",
    "pregunta dificil bro",
    "necesito mas ram mental",
    "procesando respuesta...",
    "resultado: ni idea",
]


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
        await general_channel.send("hola lindos")
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

    global s

    replace = "aeouáéóúAEOUÁÉÓÚ"

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

    if bot.user in msg.mentions:

        if "?" in msg.content:
            await msg.reply(random.choice(questions_r))
        else:
            if message.content == "":
                
                await msg.reply(random.choice(vacilones))

    if msg.channel.id == 997124912475021462:

        if "demonio 0x1" in msg.content:

            original = await msg.channel.fetch_message(
                msg.reference.message_id
            )

            send = ""

            for c in original.content:

                if c in replace:
                    send += "i" if c.islower() else "I"
                else:
                    send += c

            await msg.reply(send)

    await bot.process_commands(msg)
    
keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
