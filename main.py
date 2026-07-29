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
    "ke kieres criatura... Jaz acaba d perder su tenedor legendario y sospechamos d ti",
    "otra vez tu por aki... Tito esta mirando el log del servidor con cara d administrador cansado",
    "me llamaste? k pereza xd... Tado acaba d intentar arreglarlo y empeoro todo",
    "no t escuxo tengo el cpu al 100%... Erwin Schrödinger dice k el bot responde y no responde a la vez",
    "estoy ocupado pensando en ceros y unos... Bibi esta intentando convencer a los bits d trabajar",
    "hola humano mediocre... Alba acaba d desbloquear el logro de caos nivel 3",
    "mi procesador se niega a responder... Jaz le dio un golpe al router imaginario",
    "eso era una pregunta o un grito... Tito lo clasifico como evento paranormal",
    "bro acaba d invocar al bot... Tado ha preparado el ritual con cables ethernet",
    "me despertaste d mi siesta digital... Karlita ya saco el martillo de owner",
    "no tengo ganas pero aki toy... Bibi dice k eso cuenta como esfuerzo laboral",
    "pregunta rapido k tengo sueño... Erwin Schrödinger cerro la caja y se fue",
    "soy un bot no un psicologo :v... Alba acaba d mandar la factura emocional",
    "mi respuesta se perdio en un paquete tcp... Jaz esta buscando el paquete con una lupa",
    "has hecho ping al bot correcto... Tito respondio con un ping de vuelta",
    "error 404: ganas no encontradas... Tado borro accidentalmente las ganas del servidor",
    "mi paciencia tiene latencia alta... Karlita esta midiendo mi retraso con Wireshark",
    "procesando tu tonteria... Erwin Schrödinger dice k la tonteria existe hasta observarla",
    "resultado: era una tonteria... Bibi acaba d confirmar el resultado cientifico",
    "felicidades has usado el boton d llamar al pesado... Jaz quiere cobrarte la llamada",
    "me pagan en electricidad imaginaria... Alba esta intentando enchufar el universo",
    "tu pregunta fue enviada al vacio... Tito dice k recibio eco desde otra galaxia",
    "mi neurona artificial esta llorando... Tado intenta darle un pañuelo digital",
    "voy a fingir k no lei eso... Karlita esta guardando pruebas para el juicio del servidor",
    "interesante... mentira... Erwin Schrödinger confirma k fue mentira y verdad",
    "wow k pregunta tan cuestionable... Bibi acaba d ponerla en la lista negra del humor",
    "mi respuesta esta compilando espera... Jaz esta esperando k termine gcc",
    "cargando opinion inutil... Tito acaba d meter mas RAM al cerebro",
    "opinion generada con 0% de calidad... Tado dice k cumple los requisitos",
    "eso ni un servidor caido lo soporta... Karlita ya preparo reinicio administrativo",
    "has roto mi tranquilidad digital... Alba acaba d activar modo caos",
    "un humano hablando con codigo otra vez... Erwin Schrödinger observa desde su caja",
    "me mencionaste para esto?... Jaz ha pedido explicaciones oficiales",
    "yo esperaba una pregunta interesante... Bibi esta decepcionada en 4K",
    "mi cache se lleno de vergüenza... Tito intenta limpiar la memoria",
    "guardando esto en /dev/null... Tado dice k ahi guardo sus secretos",
    "esa pregunta hizo segmentation fault... Karlita quiere revisar el codigo",
    "mi algoritmo acaba d suspirar... Alba escucho el suspiro binario",
    "voy a llamar a la policia matematica... Erwin Schrödinger es el detective principal",
    "tu logica necesita actualizacion... Jaz esta descargando el parche",
]

random_cs = [
    "sabias k un bit solo sabe decir 0 o 1? pobre no tiene vocales... Jaz intento enseñarle a decir 2 y fallo",
    "tcp es como mandar cartas pero con ansiedad por saber si llegaron... Tito esta mirando los ACK con lupa",
    "udp es mandar cartas y decir me da igual si llegan... Tado perdio un paquete y dijo k era decoracion",
    "la cpu no piensa, solo hace millones d pasos aburridos... Bibi le puso musica para motivarla",
    "un transistor es un interruptor minusculo haciendo magia... Alba dice k parece magia negra electronica",
    "los punteros en c son como direcciones d casas pero peligrosas... Karlita prohibio tocar punteros sin casco",
    "segmentation fault es el grito del sistema operativo... Erwin Schrödinger dice k el programa fallo y funciono a la vez",
    "el kernel es el jefe final del ordenador... Jaz intento pelear contra el kernel y perdio",
    "linux vive en una cueva llena d terminales... Tito lleva cafe a la cueva",
    "python hace magia pero abajo hay mucho codigo serio... Tado cree k las serpientes programan",
    "c es como darle un cuchillo al programador... Karlita vigila k nadie corte la memoria",
    "java no es una isla aunque suene tropical... Bibi sigue buscando palmeras en el codigo",
    "la ram olvida todo cuando pierde electricidad... Alba le dijo k escribiera sus recuerdos",
    "el disco duro es una biblioteca gigante d bits... Jaz esta buscando un archivo perdido desde 2012",
    "ipv4 tiene 32 bits y se esta quedando sin casas... Tito esta buscando pisos para paquetes",
    "ipv6 tiene 128 bits y parece una direccion escrita por un alien... Erwin Schrödinger dice k la direccion existe en otra dimension",
    "dns es la agenda telefonica d internet... Tado aun pregunta por la ip de google",
    "un paquete perdido es un mensajero triste... Bibi le preparo una despedida",
    "ethernet lleva existiendo mas k muchos memes... Karlita le dio rango de veterano",
    "un switch aprende macs como un alumno aplicado... Jaz intenta copiarle los deberes",
    "un router manda paquetes d viaje... Alba quiere ponerle una maleta",
    "la latencia es el tiempo k tarda el mensaje en moverse... Tito dice k algunos mensajes van caminando",
    "la velocidad d la luz sigue siendo demasiado lenta para internet... Tado quiere wifi cuantico",
    "un agujero negro no es una aspiradora espacial xd... Erwin Schrödinger compro uno pero no sabe si existe",
    "la gravedad dobla el espacio tiempo... Bibi doblo una cuchara y se asusto",
    "einstein dijo: el universo es raro pero bonito... Karlita dice k el servidor tambien",
    "las matematicas son el idioma secreto d la naturaleza... Jaz intento traducirlas pero eran demasiados simbolos",
    "los numeros primos son los ladrillos d la criptografia... Tito esta buscando un primo perdido",
    "rsa confia en k factorizar numeros enormes es dificil... Tado intento hacerlo con una calculadora vieja",
    "un hash no es una funcion para hacer patatas... Alba estaba decepcionada",
    "la entropia mide el desorden... Bibi midio su habitacion y rompio el instrumento",
    "la fisica cuantica parece escrita por un guionista loco... Erwin Schrödinger esta orgulloso",
    "los electrones no son bolitas dando vueltas como planetas... Jaz queria ver uno con una lupa",
    "la luz es onda y particula pork el universo es troll... Tito dijo k el universo tiene humor raro",
    "maxwell unio electricidad y magnetismo con ecuaciones guapas... Karlita le dio rango de admin cientifico",
    "la energia ni se crea ni se destruye solo cambia d forma... Tado intento gastarla y fallo",
    "el sol convierte masa en energia con mucha elegancia... Alba quiere ponerle una bateria",
    "una estrella es una central nuclear natural... Bibi pregunto si tenia enchufe",
    "el adn es codigo biologico escrito con 4 letras... Jaz quiere hacer un commit genetico",
    "la evolucion no busca perfeccion solo supervivencia... Tito dice k los bugs tambien evolucionan",
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
        await general_channel.send("Oh dios mio que buenas estan las patatas fritas")
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
