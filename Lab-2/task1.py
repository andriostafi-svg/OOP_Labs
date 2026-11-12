# Завдання 1, варіант 13: факторіал числа 15
n = 15
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")
