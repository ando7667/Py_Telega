import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


but_game = InlineKeyboardButton(text="Поиграем", callback_data="game")
but_exit = InlineKeyboardButton(text="Посчитаем", callback_data="calc")
menu_start = InlineKeyboardMarkup(row_width=2)
menu_start.add(but_game, but_exit)

but_human = InlineKeyboardButton(text="Человек", callback_data="human")
but_bot = InlineKeyboardButton(text="Бот", callback_data="bot")
inline_menu_gm = InlineKeyboardMarkup(row_width=2)
inline_menu_gm.add(but_human, but_bot)


but_number = InlineKeyboardButton(text="Обычные числа", callback_data="calc_number")
but_complex = InlineKeyboardButton(text="Комплексные числа", callback_data="calc_complex")
inline_menu_mcalc = InlineKeyboardMarkup(row_width=2)
inline_menu_mcalc.add(but_number, but_complex)


but_1 = InlineKeyboardButton(text="1", callback_data="calc_1")
but_2 = InlineKeyboardButton(text="2", callback_data="calc_2")
but_3 = InlineKeyboardButton(text="3", callback_data="calc_3")
but_4 = InlineKeyboardButton(text="4", callback_data="calc_4")
but_5 = InlineKeyboardButton(text="5", callback_data="calc_5")
but_6 = InlineKeyboardButton(text="6", callback_data="calc_6")
but_7 = InlineKeyboardButton(text="7", callback_data="calc_7")
but_8 = InlineKeyboardButton(text="8", callback_data="calc_8")
but_9 = InlineKeyboardButton(text="9", callback_data="calc_9")
but_0 = InlineKeyboardButton(text="0", callback_data="calc_0")

but_minus = InlineKeyboardButton(text="-", callback_data="calc_-")
but_plus = InlineKeyboardButton(text="+", callback_data="calc_+")
but_mul = InlineKeyboardButton(text="*", callback_data="calc_*")
but_del = InlineKeyboardButton(text="/", callback_data="calc_/")
but_remd = InlineKeyboardButton(text="%", callback_data="calc_%")
but_divc = InlineKeyboardButton(text="//", callback_data="calc_//")
but_pow = InlineKeyboardButton(text="**", callback_data="calc_**")
but_sqrt = InlineKeyboardButton(text="SQRT", callback_data="calc_sqrt")

but_enter = InlineKeyboardButton(text="=", callback_data="calc_=")
but_dot = InlineKeyboardButton(text=".", callback_data="calc_.")


inline_menu_calc_n = InlineKeyboardMarkup(row_width=4)
inline_menu_calc_n.add(but_7, but_8, but_9, but_minus, but_plus)
inline_menu_calc_n.add(but_4, but_5, but_6, but_del, but_mul)
inline_menu_calc_n.add(but_1, but_2, but_3, but_remd, but_divc)
inline_menu_calc_n.add(but_0, but_dot, but_enter, but_pow)

inline_menu_calc_c = InlineKeyboardMarkup(row_width=4)
inline_menu_calc_c.add(but_7, but_8, but_9, but_minus, but_plus)
inline_menu_calc_c.add(but_4, but_5, but_6, but_del, but_mul)
inline_menu_calc_c.add(but_1, but_2, but_3, but_pow)
inline_menu_calc_c.add(but_0, but_dot, but_enter)
