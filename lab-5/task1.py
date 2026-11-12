# Завдання 1. Обробка ділення на нуль
a = 5
b = 0
print(f"a = {a}, b = {b}")
try:
    print("Результат:", a / b)
except ZeroDivisionError:
    print("Помилка: ділення на нуль!")
