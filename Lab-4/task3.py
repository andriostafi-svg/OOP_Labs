# Завдання 3. Робота з курсором файлу
with open("lines.txt", "w", encoding="utf-8") as f:
    f.write("Перший рядок\nДругий рядок\nТретій рядок\n")

with open("lines.txt", "r", encoding="utf-8") as f:
    print("Перший рядок:", f.readline().strip())
    print("Позиція курсора:", f.tell())
    f.seek(0)
    print("Весь текст:")
    print(f.read())
