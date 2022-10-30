from logger import logger_history as cl


def sum(a, b):
    cl("Выполнена операция", f'{a} + {b}', a + b)
    print(f"Результат = {a + b}")


def sub(a, b):
    cl("Выполнена операция", f'{a} - {b}', a - b)
    print(f"Результат = {a - b}")


def mult(a, b):
    cl("Выполнена операция", f'{a} * {b}', a * b)
    print(f"Результат = {a * b}")


def div(a, b):
    if b:
        cl("Выполнена операция", f'{a} / {b}', a / b)
        print(f"Результат = {a / b}")
    else:
        cl("Внимание", "Деление на ноль", "")


def remainder_div(a, b):
    cl("Выполнена операция", f'{a} % {b}', a % b)
    print(f"Результат = {a % b}")


def div_compl(a, b):
    cl("Выполнена операция", f'{a} // {b}', a // b)
    print(f"Результат = {a // b}")


def pow(a, b):
    cl("Выполнена операция", f'{a} ** {b}', a ** b)
    print(f"Результат = {a ** b}")


def sqrt_pow(a, b):
    if b:
        cl("Выполнена операция", f'{a} sqrt^{b}', f"{(a ** (1/b)):.2f}")
        print(f"Результат = {(a ** (1/b)):.2f}")
    else:
        cl("Внимание", "Корень со степьнью 0", "")

def fun(oper , num1, num2 ):
    oper(num1, num2)