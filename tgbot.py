import collections.abc

collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping
collections.Iterable = collections.abc.Iterable
collections.MutableSet = collections.abc.MutableSet
collections.Callable = collections.abc.Callable




import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, CallbackQueryHandler, Filters

BOT_TOKEN = "6726913085:AAHo-KrZj_Oh526PqwdueLS596e4tl6QsEM"
#API_URL = "http://127.0.0.1:8000"  # Укажите актуальный адрес вашего FastAPI сервера

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне голосовое сообщение.')

def process_voice_message(update: Update, context: CallbackContext) -> None:
    # Проверяем, является ли сообщение голосовым
    if update.message.voice:
        # Получаем информацию о голосовом сообщении
        voice = update.message.voice
        file_id = voice.file_id

        # Сохраняем информацию о файле в контексте пользователя
        context.user_data['file_id'] = file_id

        # Отправляем голосовое сообщение обратно
        update.message.reply_voice(voice.file_id)

        # Отправляем клавиатуру с оценками от 1 до 5
        keyboard = [
            [InlineKeyboardButton("1", callback_data='1'),
             InlineKeyboardButton("2", callback_data='2'),
             InlineKeyboardButton("3", callback_data='3')],
            [InlineKeyboardButton("4", callback_data='4'),
             InlineKeyboardButton("5", callback_data='5')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Отправляем клавиатуру пользователю
        update.message.reply_text('Выберите оценку:', reply_markup=reply_markup)

        # Отправляем данные голосового сообщения на внешний FastAPI сервер
        #api_response = send_voice_to_api(file_id)
        #if api_response:
            # Если получен ответ от API, отправляем его пользователю
        #    update.message.reply_text(f"API вернуло: {api_response}")
        #else:
        #    update.message.reply_text("Не удалось получить ответ от API.")
    #else:
    #    update.message.reply_text('Это не голосовое сообщение.')

def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # Обработка нажатия кнопки
    rating = query.data

    # Получаем информацию о файле из контекста пользователя
    file_id = context.user_data.get('file_id')

    query.edit_message_text(f"Вы выбрали оценку {rating}. Спасибо за ваш отзыв!")

    # Здесь вы можете использовать file_id для дополнительной обработки файла (например, сохранение на сервере)

def send_voice_to_api(file_id: str) -> str:
    try:
        # Здесь вы можете выполнить HTTP-запрос к вашему FastAPI серверу, передавая file_id в теле запроса
        # Пример запроса:
        response = requests.post(f"{API_URL}/process_voice", json={"file_id": file_id})
        if response.status_code == 200:
            return response.json().get('result', '')
        else:
            return f"Ошибка при отправке запроса: {response.status_code}"
    except Exception as e:
        return f"Произошла ошибка: {e}"

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.voice & ~Filters.command, process_voice_message))
    dp.add_handler(CallbackQueryHandler(button_click))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
