# Завдання 2, варіант 13: перевірити, чи число 14 просте
n = 14
is_prime = n > 1
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        print(f"{n} ділиться на {i}")
        break
if is_prime:
    print(f"{n} - просте число")
else:
    print(f"{n} - не просте число")
