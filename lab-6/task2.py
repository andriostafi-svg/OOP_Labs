# Завдання 2. Генератор випадкових чисел
import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Список:", numbers)
print("Середнє:", sum(numbers) / len(numbers))
print("Максимум:", max(numbers))
print("Мінімум:", min(numbers))
print("Парних чисел:", len([n for n in numbers if n % 2 == 0]))
