import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
kill_menu = ReplyKeyboardRemove(selective=False)


but_game = InlineKeyboardButton(text="Поиграем", callback_data="game")
but_exit = InlineKeyboardButton(text="Посчитаем", callback_data="calc")
menu_start = InlineKeyboardMarkup(row_width=2)
menu_start.add(but_game, but_exit)


but_human = InlineKeyboardButton(text="Человек", callback_data="human")
but_bot = InlineKeyboardButton(text="Бот", callback_data="bot")
inline_menu_gm = InlineKeyboardMarkup(row_width=2)
inline_menu_gm.add(but_human, but_bot)
