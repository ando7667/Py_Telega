import telebot
from main import bot
from time import sleep as s
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

kr = chr(10060)
nul = chr(11093)

board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']

win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

# режим игры: 0 - не определено; 1 - Человек vs Человек;  2 - Человек vs Бот
mode = 0

# текущий игрок: 0 - не определен; 1 - Игрок 1 (x) ; 2  - Игрок 2 (o)
player = 0

count = 0


def rnd_player():
    return random.randint(1, 2)


def draw_board(call, sz: int = 3):
    global player
    global mode
    st = "Ходит "
    if mode == 2 and player == 2:
        st += "Бот"
    else:
        st += f"Игрок {player}"

    print(st, f"player={player}, mode= {mode}")
    g_keyboard = InlineKeyboardMarkup(row_width=sz)

    for i in range(sz):
        g_key1 = InlineKeyboardButton(text=board[i * 3], callback_data=board[i * 3])
        g_key2 = InlineKeyboardButton(text=board[i * 3 + 1], callback_data=board[i * 3 + 1])
        g_key3 = InlineKeyboardButton(text=board[i * 3 + 2], callback_data=board[i * 3 + 2])
        g_keyboard.add(g_key1, g_key2, g_key3)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=g_keyboard)
    #    bot.send_message(call.message.chat.id, text=st, reply_markup=g_keyboard)
    bot.send_message(call.message.chat.id, text=st)
    if mode == 2 and player == 2:
        input_bot(call)


def player_input(call, inp):
    global player
    global mode
    global count

    inp = int(inp)
    check = board[inp - 1]
    if check not in (kr, nul):
        board[inp - 1] = kr if player == 1 else nul
        player = 1 if player == 2 else 2
        count += 1
        draw_board(call)
        if count > 3:
            winp = if_win()
            if winp:
                bot.send_message(call.message.chat.id,
                                 text=f"Победил Игрок {player} [{winp}] на {count} ходу !{chr(127874)}")

        if count > 7:
            bot.send_message(call.message.chat.id, text=f"Ходы закончились! Ничья !{chr(127927)}")
    else:
        print("Эта клетка уже занята")
        bot.send_message(call.message.chat.id, text=f"Эта клетка уже занята {chr(129300)}")


def input_bot(call):
    n = []
    for i, v in enumerate(board):
        if v not in (kr, nul):
            n.append(v)
    player_input(call, int(*random.choices(n)))


def if_win():
    n = [board[x[0]] for x in win if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n


def main(call, flag: int = 0, md: int = 0):
    global mode
    global player
    global count
    global board
    bot.send_message(call.message.chat.id, text="Игра крестики-нолики")
    if flag == 0 or player == 0:
        player = rnd_player()
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        count = 0
    else:
        if flag:
            player = flag
    if md:
        mode = md
    draw_board(call=call)
