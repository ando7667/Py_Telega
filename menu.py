import telebot
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

    bot.infinity_polling(interval=0, timeout=20)


@bot.message_handler(commands=['start'])
def start_message(message):
    lg.logger_history(f"{data()} - id:{message.from_user.id}",
                      f"{message.from_user.first_name} {message.from_user.last_name} - ", f"{message.text}")
    bot.send_message(message.chat.id, text="Чем займёмся?", reply_markup=view.menu_start)


def data():
    return datetime.datetime.now().strftime('%d-%m-%Y %H:%M')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    st1 = f" - id:{call.from_user.id} {call.from_user.first_name} {call.from_user.last_name} - "
    numb = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    match call.data:
        case 'calc':
            lg.logger_history(st1, "Запуск калькулятора", "")
            bot.send_message(call.message.chat.id, text="Калькулятор")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, text="Задайте режим работы")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=view.inline_menu_mcalc)
        case 'calc_number':
            lg.logger_history(st1, "Калькулятор, режим работы с обычными числами", "")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, text="Выбирите противника")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=view.inline_menu_calc_n)
        case 'calc_complex':
            lg.logger_history(st1, "Калькулятор, режим работы с комплексными числами", "")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, text="Выбирите противника")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=view.inline_menu_calc_c)
        case 'game':
            lg.logger_history(st1, "Вход в Игру XvsO", "")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, text="Выбирите противника")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=view.inline_menu_gm)
        case 'human':
            lg.logger_history(st1, "Игра с человеком", "")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            gm.main(call=call, flag=0, md=1)
        case 'bot':
            lg.logger_history(st1, "Игра с Ботом", "")
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            gm.main(call=call, flag=0, md=2)
        case a if a in numb:
            print(f"call.data= {call.data}")
            gm.gm_step(call, call.data)
        case 'win':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


@bot.message_handler(content_types=['text'])
def send_text(message):
    lg.logger_history(f"{data()} - id:{message.from_user.id}",
                      f"{message.from_user.first_name} {message.from_user.last_name}", f" написал: {message.text}")
    st1 = f"Ты написал: {message.text}"
    bot.reply_to(message, text=st1)

