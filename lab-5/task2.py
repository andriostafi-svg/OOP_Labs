# Завдання 2. Обробка помилок введення
text = "abc"
print("Введено:", text)
try:
    number = int(text)
    print("Число:", number)
except ValueError:
    print("Помилка: введено нечислове значення!")
finally:
    print("Програма завершена.")
