from datetime import datetime as dtime
from time import time


def logger_history(st1, st2, st3):
    tm = dtime.now().strftime('%d.%m.%y %H:%M')
    with open('history.log', 'a', encoding="utf-8") as lf:
        lf.write('{} {} {} {}\n'.format(tm, st1, st2, st3))
