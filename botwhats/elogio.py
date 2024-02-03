import telebot
import requests
import json
import pytube
import moviepy.editor
import os
import re
#import date
from telebot import TeleBot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup

# API_KEY_TELEBOT
CHAVE_API = "6703116249:AAFC2l1Ymnj-x4wcrEzfX6vm66dpAbJwO9M"
bot = telebot.TeleBot(CHAVE_API)

# API_KEY_NASA
#pcde98MI37hc4MPsYfXSOXYNsk604INiR1EQUY2q

#====================API====================
#-----------------DOWNLOAD_MP3--------------
link_video = input()
def download_musica(link_video,pasta_arquivo):
    link = pytube.YouTube(link_video)
    diretorio = pasta_arquivo
    download = link.streams.filter(only_audio = True).first().download(diretorio)
    for file in os.listdir(diretorio):
        if re.search("mp4",file):
            mp4_path = os.path.join(diretorio,file)
            mp3_converte = os.path.join(diretorio,os.path.splitext(file)[0]+".mp3")
            arquivo_mp3 = moviepy.editor.AudioFileClip(mp4_path)
            arquivo_mp3.write_audiofile(mp3_converte)
            os.remove(mp4_path)

def download_video(link_video,pasta_arquivo):
    link = link_video
    diretorio = pasta_arquivo
    youtube = pytube.YouTube(link)
    download = youtube.streams.filter(progressive = True, file_extension="mp4").first().download(diretorio)

#-------------------------------------------

#--------------elogio----------------------
elogio = requests.get("https://api.adviceslip.com/advice")
elogio = elogio.json()
elogio_elogio = elogio['slip']["advice"]

#------------------------------------------
#==========================================

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

#-----------------BOTÕES---------------------
# INICIAL(help, menu, prox)
def inicial_button():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(
        InlineKeyboardButton("🧰HELP", callback_data="help"),
        InlineKeyboardButton("SERVIÇOS", callback_data="servicos"),
        InlineKeyboardButton("PROX▶", callback_data="prox")
    )
    return markup

# HELP
def help_button():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("COMANDS", callback_data="comands"),
        InlineKeyboardButton("SUPORT", callback_data="suport")
    )
    return markup

# SERVICE
def services_button():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("NASA🌎", callback_data="NASA"),
        InlineKeyboardButton("MP3🎼", callback_data="mp3"),
        InlineKeyboardButton("MP4🎞", callback_data="mp4")
    )
    return markup

# SERVICES NASA
def services_button():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("APOD", callback_data="apod"), 
        InlineKeyboardButton("ASTEROIDES", callback_data="asteroides"), 
        InlineKeyboardButton("APOD", callback_data="apod"), 
        InlineKeyboardButton("APOD", callback_data="apod"), 
    )
    return markup


# RUN
def run_button():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("RUN", callback_data="run"),
    )
    return markup

# NASA OPNIONS
def nasa_button():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("PICTURE OF DAY", callback_data="picture"),
        InlineKeyboardButton("RUN", callback_data="run"),
    )
    return markup
#-------------------------------------------

#---------------BUTTON_FUNC-----------------
@bot.callback_query_handler(func=lambda call:True)
def query(call):
    if call.data=="help":
        botao1(call.message)
    elif call.data=="servicos":
        botao2(call.message)
    elif call.data=="suport":
        botao4(call.message)    
    elif call.data=="prox":
        botao3(call.message)
    elif call.data=="run":
        botao4(call.message)
    elif call.data=="nasa":
        botao4(call.message)
#-------------------------------------------

# BOTAO HELP
@bot.message_handler(commands=['help'])
def botao1(message):
    text2 = """
    Com oq posso lhe ajudar hoje na sua busca nobre guerreiro ???
    """                                       
    bot.send_message(message.chat.id, text2,  reply_markup=help_button())

# BOTAO SERVICOS
@bot.message_handler(commands=['servicos'])
def botao2(message):
    text = "Ola denovo!!!! aqui é o TenorioBOT como posso lhe ajudar hoje???"
    bot.send_message(message.chat.id, text, reply_markup=services_button())

# BOTAO PROX
IMAGE_LINK3 = "https://t.ctcdn.com.br/_B1jIBlX0oK1N0ZEf0ZdHc0x4nc=/1024x0/smart/i344447.png"
@bot.message_handler(commands=['prox'])
def botao3(message):
    bot.send_message(message.chat.id, elogio_elogio)
    bot.message_handler(commands=['image'])
    bot.send_photo(message.chat.id, IMAGE_LINK3, reply_markup=run_button())

# BOTAO SUPORT
IMAGE_LINK1 = "https://i.pinimg.com/236x/f9/b9/cc/f9b9cc13ed854ec0c3282b572fdf1e03.jpg"
@bot.message_handler(commands=['suport'])
def botao4(message):
    bot.message_handler(commands=['image'])
    bot.send_photo(message.chat.id, IMAGE_LINK1)
    bot.send_message(message.chat.id, """
    Mande Email pro suporte atraves do:
            alant3387@yahoo.com""")

# BOTAO RUN
@bot.message_handler(commands=['run'])
def botao5(message):
    bot.send_message(message.chat.id, """
    Iniciando programa...""",)

# BOTAO NASA

@bot.message_handler(commands=['nasa'])
def botao6(message):
    picture_day = requests.get("https://api.nasa.gov/planetary/apod?api_key=pcde98MI37hc4MPsYfXSOXYNsk604INiR1EQUY2q")
    picture_day = picture_day.json()
    title = picture_day['title']
    hdurl = picture_day['hdurl']
    explanation = picture_day['explanation']
    date = picture_day['date']
    picture = hdurl
    bot.message_handler(commands=['image'])
    bot.send_photo(message.chat.id,title, """       
    """, picture, explanation)
    bot.send_message(message.chat.id, date)

#-----------------botao---------------------

#-------------message_inicial---------------
def verificar(mensagem):
    return True
@bot.message_handler(func=verificar)
def responder(message):
# https://openai.com/
    text = """
by TNorioh: https://github.com/TNorioh
Official Channel: https://t.me/tenoriobots
creator BOT: @tenoriohhh

Oii!!!!! aqui é o Tenorios, Escolha uma dos commandos a baixo para prosseguir:  

    """
    bot.send_message(message.chat.id, text, reply_markup=inicial_button())


bot.polling()