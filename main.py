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

pegando = [
    "*le pega con una chancla cuantica a ",
    "*le da un sape galactico a ",
    "*le pega con un baguette mojado a ",
    "*le mete un zape del paleolitico a ",
    "*le pega con una impresora hp furiosa a ",
    "*le tira un teclado mecanico encima a ",
    "*le da un sopapo intercontinental a ",
    "*le pega con un router cisco del 2009 a ",
    "*le da un coscorron nuclear a ",
    "*le pega con una patata overclockeada a ",
    "*le lanza una chancla orbitando saturno a ",
    "*le pega con una tostadora filosofica a ",
    "*le da un puñetazo de gomaespuma a ",
    "*le pega con un calcetin humedo legendario a ",
    "*le mete un guantazo de minecraft a ",
    "*le pega con un libro de matematicas gordisimo a ",
    "*le da una colleja wifi 6 a ",
    "*le pega con un monitor crt de 40 kilos a ",
    "*le tira una croqueta tactica a ",
    "*le pega con un palo de escoba premium a ",
    "*le da un soplamocos ultrasonico a ",
    "*le pega con una sardina medieval a ",
    "*le mete un zape bluetooth a ",
    "*le pega con un ladrillo intelectual a ",
    "*le da una hostia de carton reciclado a ",
    "*le pega con un diccionario rumano-español a ",
    "*le lanza una berenjena balistica a ",
    "*le pega con una regla de 30 cm del infierno a ",
    "*le da un puñetazo administrativamente incorrecto a ",
    "*le pega con una silla gamer sin ruedas a ",
    "*le tira un modem adsl nostalgico a ",
    "*le pega con una baguette francesa certificada a ",
    "*le da un zape tan fuerte q cambia de region a ",
    "*le pega con un disco duro de 80 gb a ",
    "*le mete un sopapo patrocinado por tito a ",
    "*le pega con una chancla doblada +5 a ",
    "*le da un puñetazo con lag a ",
    "*le pega con una botella de agua vacia dramatica a ",
    "*le tira un router q no da internet a ",
    "*le pega con una cuchara legendaria a ",
    "*le da un zape certificado por jaz lonjas mortales a ",
    "*le pega con un cable ethernet enrollado a ",
    "*le tira una pizza hawaiana prohibida a ",
    "*le pega con una calculadora casio enfadada a ",
    "*le da una colleja q se oye en marte a ",
    "*le pega con un manual del ccna de 900 paginas a ",
    "*le lanza una chancla boomerang a ",
    "*le pega con una almohada llena de ladrillos a ",
    "*le da un sape patrocinado por agarvv roba cobre a ",
    "*le pega con una barra de pan endurecida a ",
    "*le tira un monitor azul de windows a ",
    "*le pega con un hamster cuantico furioso a ",
    "*le da un zape q reinicia el dns a ",
    "*le pega con un ventilador rgb poseido a ",
    "*le tira una tortilla francesa aerodinamica a ",
    "*le pega con un raton gamer sin pilas a ",
    "*le da una hostia educada pero contundente a ",
    "*le pega con una nube comprimida a ",
    "*le tira una sandalia turbo a ",
    "*le pega con un enchufe filosofico a ",
    "*le da un zape q compila linux a ",
    "*le pega con una antena wifi oxidada a ",
    "*le tira una croqueta boomerang a ",
    "*le pega con un modem usb del jurasico a ",
    "*le da un sape de 144 hz a ",
    "*le pega con una mesa plegable epica a ",
    "*le tira una baguette supersonica a ",
    "*le pega con una patata frita titanica a ",
    "*le da una colleja certificada por karlita la owner a ",
    "*le pega con un router lleno de polvo a ",
    "*le tira un cojín agresivo a ",
    "*le pega con una cuchara de palo ancestral a ",
    "*le da un zape q cambia la mac address a ",
    "*le pega con una escoba multiversal a ",
    "*le tira un teclado q suena clac clac clac a ",
    "*le pega con una sandia tactica a ",
    "*le da un puñetazo de plastilina a ",
    "*le pega con una croqueta criogenica a ",
    "*le tira una tostadora wifi a ",
    "*le pega con un mando de la tele ancestral a ",
    "*le da una hostia diplomatica a ",
    "*le pega con una baguette doblada imposible a ",
    "*le tira una silla de plastico legendaria a ",
    "*le pega con un cable usb imposible de enchufar a ",
    "*le da un zape q actualiza la bios a ",
    "*le pega con una tortilla de patatas compacta a ",
    "*le tira un modem q hace piiiiii a ",
    "*le pega con una caja de cereales blindada a ",
    "*le da una colleja del espacio exterior a ",
    "*le pega con una barra de hierro imaginaria a ",
    "*le tira una patata ninja a ",
    "*le pega con un libro de filosofia existencialista a ",
    "*le da un sape q resetea el karma a ",
    "*le pega con una fregona hiperespacial a ",
    "*le tira un teclado membrana tristisimo a ",
    "*le pega con una croqueta cuantica de alba a ",
    "*le da un zape oscuro de jaz but oscura a ",
    "*le pega con una media tactica de tado femboy a ",
    "*le tira un manual de supervivencia de anne a ",
    "*le pega con una llave inglesa filosofica de hasiel a ",
    "*le da un sape patrocinado por daniel corp a ",
    "*le pega con una nube de helio de agarv tetillas hinchadas a ",
    "*le tira una croqueta premium de bibi a ",
    "*le pega con una baguette bendecida por karlita a ",
    "*le da un zape final boss a "
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
        await general_channel.send("tengo anvre")
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
