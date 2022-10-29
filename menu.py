from telegram import message
import logger as lg
from main import bot
import datetime
from config import chat_id
import view
import game_xo as gm


def send_to_admin():
    st1 = "Telegram бот сборка 001 от 29.10.2022"
    st2 = "Бот запущен"
    print(f"{st1}\n{data()} - {st2}")
    lg.logger_history(st1, " - ", st2)
    bot.send_message(chat_id=chat_id, text="Бот запущен\n"
                                           "Для запуска меню нажмите /start")

    bot.infinity_polling()

@bot.message_handler(commands=['start'])
def start_message(message):
    lg.logger_history(f"{data()} - id:{message.from_user.id}",
                      f"{message.from_user.first_name} {message.from_user.last_name} - ", f"{message.text}")
    bot.send_message(message.chat.id, text="Чем займёмся?", reply_markup=view.menu_start)


@bot.message_handler(content_types=['text'])
def send_text(message):
    lg.logger_history(f"{data()} - id:{message.from_user.id}",
                      f"{message.from_user.first_name} {message.from_user.last_name}", f" написал: {message.text}")
    st1 = f"Ты написал: {message.text}"
    bot.reply_to(message, text=st1)


def chese_gm(num1, num2, btn):
    if btn.data[1:2] == 'b':
        gm.main(num1, num2, btn=btn, player=int(btn.data[2:]))
    else:
        gm.btn_data(num1, num2, btn=btn, id_pair=int(btn.data[1:]))


def data():
    return datetime.datetime.now().strftime('%d-%m-%Y %H:%M')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    st1 = f" - id:{call.from_user.id} {call.from_user.first_name} {call.from_user.last_name} - "
    if call.data == 'game':
        lg.logger_history(st1, "Вход в Игру XvsO", "")
        bot.send_message(call.message.chat.id, text="Выбирите противника")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=view.inline_menu_gm)
    if call.data == 'human':
        gm.main(call, 1)
        lg.logger_history(st1, "Игра с человеком", "")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    if call.data == 'bot':
        gm.main(call, 0)
        lg.logger_history(st1, "Игра с Ботом", "")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    if call.data[:1] == '1':
        chese_gm(0, 0, call)
    if call.data[:1] == '2':
        chese_gm(0, 1, call)
    if call.data[:1] == '3':
        chese_gm(0, 2, call)
    if call.data[:1] == '4':
        chese_gm(1, 0, call)
    if call.data[:1] == '5':
        chese_gm(1, 1, call)
    if call.data[:1] == '6':
        chese_gm(1, 2, call)
    if call.data[:1] == '7':
        chese_gm(2, 0, call)
    if call.data[:1] == '8':
        chese_gm(2, 1, call)
    if call.data[:1] == '9':
        chese_gm(2, 2, call)
    if call.data == "win":
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

