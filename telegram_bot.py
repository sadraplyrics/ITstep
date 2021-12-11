import telebot

my_bot = telebot.TeleBot("<СЮДА ВЫ ВСТАВЛЯЕТЕ СВОЙ ТОКЕН>") # Создание самого бота

@my_bot.message_handler(commands=["greet"]) # Это ключевое слово, вызывающее команду
def hello(message):
    my_bot.send_message(message.chat.id, "Hello") # Эта функция выполняется при вызове команды