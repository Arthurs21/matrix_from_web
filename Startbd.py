import sqlite3
import telebot

bot = telebot.TeleBot()

conn = sqlite3.connect('Really_Good_db.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str):
    cursor.execute('INSERT INTO test (user_id, user_name) VALUES (?)',
                   (user_id, user_name))
    conn.commit()

def db_table_val1(user_id: int, user_surname: str):
    cursor.execute('INSERT INTO test (user_id, user_surname) VALUES (?, ?)',
                   (user_id, user_surname))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':

        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        try:
            db_table_val(user_id=us_id, user_name=us_name)
            bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, 'Привет! Ваше имя уде имеется в базе данных!')

    elif message.text.lower() == 'адрес':
        bot.send_message(message.chat.id, 'Привет! Введите адрес!')

    elif ('дом' in message.text) and (('район' in message.text) or ('микрорайон' in message.text)):
        print(message.text)
        us_id = message.from_user.id
        db_table_val1(user_id=us_id, user_surname=message.text)
        print('Ура')


#AArstaumri001

bot.polling(none_stop=True)