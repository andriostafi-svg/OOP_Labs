# Завдання 2. Створення текстового звіту
from datetime import date

name = "Андрій"
grade = 95
today = date.today()

with open("report.txt", "a", encoding="utf-8") as f:   # 'a' - дозапис
    f.write(f"{today} | {name} | {grade}\n")

with open("report.txt", "r", encoding="utf-8") as f:
    print(f.read())
