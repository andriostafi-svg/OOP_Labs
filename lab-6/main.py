# Завдання 3. Використання власного модуля
import list_utils

data = [5, 3, 8, 3, 1, 8, 9]
print("Список:", data)
print("Відсортований:", list_utils.sort_list(data))
print("Без дублікатів:", list_utils.remove_duplicates(data))
print("Мін і макс:", list_utils.min_max(data))
