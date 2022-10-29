from main import bot
from telebot import types
from time import sleep as s

kr = chr(10060)
nul = chr(11093)

board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def draw_board(sz: int = 3):
    print("-" * 13)
    for i in range(sz):
        print(f"| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
        print("-" * 13)


def player_input(symbol):
    while True:
        inp = input(f"введите номер клетки для {symbol} : ").replace("-", "").replace(",", ".").split(".")[0]

        if inp.isdigit() and int(inp) in range(1, 10):
            inp = int(inp)
            check = board[inp - 1]
            if check not in (kr, nul):
                board[inp - 1] = kr if symbol == "x" else nul
                break
            else:
                print("Эта клетка уже занята" + chr(129300))
        else:
            print("Ввели неверный номер клетки!")


def if_win():
    n = [board[x[0]] for x in win if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n


def main(msg, flag):
    print("Игра крестики-нолики")
    player = True
    game = True
    count = 0
    draw_board()
    while game:
        if player:
            sym = "x"
        else:
            sym = "o"
        player_input(sym)
        draw_board()
        if count > 3:
            winp = if_win()
            if winp:
                game = False
            else:
                game = True
        if count > 7:
            print("Ходы закончились! Ничья !" + chr(127927))
            break
        player = not player
        count += 1

    print(f"Победил {winp} на {count} ходу !" + chr(127874))
