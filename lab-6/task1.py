# Завдання 1. Калькулятор на функціях
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

power = lambda a, b: a ** b   # лямбда-функція

x, y = 8, 2
print(f"{x} + {y} =", add(x, y))
print(f"{x} - {y} =", sub(x, y))
print(f"{x} * {y} =", mul(x, y))
print(f"{x} / {y} =", div(x, y))
print(f"{x} ** {y} =", power(x, y))
