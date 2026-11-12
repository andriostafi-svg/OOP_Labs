# Завдання 1. Обробка оцінок студентів
grades = [85, 90, 78, 92, 88]
print("Оцінки:", grades)
print("Максимальна:", max(grades))
print("Мінімальна:", min(grades))
print("Середня:", sum(grades) / len(grades))
grades.sort()
print("Відсортовані:", grades)
grades.append(95)          # додаємо нову оцінку
grades.remove(min(grades)) # видаляємо найнижчу
print("Після змін:", grades)
count = len([g for g in grades if g > 80])
print("Оцінок вище 80:", count)
