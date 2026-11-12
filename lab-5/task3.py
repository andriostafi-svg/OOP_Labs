# Завдання 3. Робота з файлами та обробка винятків
f = None
print("Спроба відкрити файл...")
try:
    f = open("data.txt", "r", encoding="utf-8")
    print("Вміст:", f.read())
except FileNotFoundError:
    print("Файл не знайдено. Створюємо новий.")
    f = open("data.txt", "w", encoding="utf-8")
    f.write("Файл створено автоматично.")
finally:
    if f:
        f.close()
    print("Файл закрито.")
