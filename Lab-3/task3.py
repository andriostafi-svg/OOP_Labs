# Завдання 3. Підрахунок унікальних елементів
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = set(numbers)
print("Список:", numbers)
print("Унікальні елементи:", unique)
print("Кількість унікальних:", len(unique))
repeat = [x for x in unique if numbers.count(x) > 1]
print("Повторюються:", repeat)
