import telebot
import config
import webbrowser
from telebot import types
import requests
TOKEN='6726913085:AAHo-KrZj_Oh526PqwdueLS596e4tl6QsEM'
bot=telebot.TeleBot(config.TOKEN)

API=''

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, пупсик! <u> Ты отлично выглядишь! </u> Протестируй меня ;)',parse_mode='html')

@bot.message_handler(commands=['site'])
def site(message):
    video_url = 'https://donstu.ru'
    bot.send_message(message.chat.id, video_url)


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, "<em>Help informationd </em>",parse_mode='html')
@bot.message_handler(commands=['helperforrazrab'])
def start(message):
    bot.send_message(message.chat.id, message)

#########################


@bot.message_handler(content_types=['audio','voice'])
def get_audio(message):
    #####################
    #voice = update.message.voice
    ###file_id = voice.file_id
    file_info = bot.get_file(message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
    #voise=message.voice
    #requests
    #file_info = bot.get_file(message.voice.file_id)
    #####################
    markap = types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton('1',callback_data='1')
    btn2=types.InlineKeyboardButton('2',callback_data='2')
    btn3=types.InlineKeyboardButton('3',callback_data='3')
    btn4=types.InlineKeyboardButton('4',callback_data='4')
    btn5=types.InlineKeyboardButton('5',callback_data='5')

    markap.row(btn1,btn2,btn3,btn4,btn5)
    bot.reply_to(message,'Oцени меня !😋',reply_markup=markap)
    #vise=voise.decode('utf-8')
    bot.send_message(message.from_user.id,file_info,file)

@bot.callback_query_handler(func=lambda callback:True)
def otvetosenka(callback):
    if callback.data=='1' or callback.data=='2'  or callback.data=='3' :
        bot.edit_message_text(f'Вы оценили нас как "{callback.data}" Спасибо за oтвет ! В следующий раз всё будет намного лучше !😅',callback.message.chat.id,callback.message.message_id)
    else:
        bot.edit_message_text(f'Вы оценили нас как "{callback.data}"Спасибо за oтвет ! Мы рады ,что вам понравилось!🤩',callback.message.chat.id,callback.message.message_id)

#bot.send_voice(message.from_user.id,vois-название преременой гдне гс) - кидает гс

############################################
@bot.message_handler()
def texte(message):
    if message.text.lower()=='иди нахуй' or message.text.lower()=='иди в жопу' :
        bot.send_message(message.chat.id, '<b>ЭЭЭЭЭЭй, это обидно !!!!!!:(</b>',parse_mode='html')
    elif message.text.lower()=='привет'or message.text.lower()=='hello'or message.text.lower()=='чертила!':
        if message.from_user.id==1361180524:
            bot.send_message(message.chat.id, '<b> Привет, о Алина ! Пиздуй учить конспекты!</b> ',parse_mode='html')
        elif message.from_user.id==1928674151:
            bot.send_message(message.chat.id, '<b> КАМИЛА ТЫ ЗАДОЛБЁШЬ С ГРАМАТИКОЙ </b> ',parse_mode='html')
        elif message.from_user.id==920772386:
            bot.send_message(message.chat.id, '<u>  ЭКСТРЕМИСТКА! привет чё как ;) </u> ',parse_mode='html')
        elif message.from_user.id==1425393372:
            bot.send_message(message.chat.id, '<em> С тебя эклер >:3 (предлагаю захуярить Алисину англичанку)</em> ',parse_mode='html')
        else :
            bot.send_message(message.chat.id, f'Привет,<b>{message.from_user.first_name} {message.from_user.last_name} </b> , ты отлично выглядишь ;)',parse_mode='html')
    else: bot.reply_to(message, ' Прости я других команд ещё не знаю',parse_mode='html')



 





bot.polling(none_stop=True)