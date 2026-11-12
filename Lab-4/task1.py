# Завдання 1. Підрахунок рядків і слів у файлі
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("Python - мова програмування.\nВона проста і зручна.\nРобота з файлами.\n")

with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

words = sum(len(line.split()) for line in lines)
print("Кількість рядків:", len(lines))
print("Кількість слів:", words)
