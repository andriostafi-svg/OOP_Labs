# Завдання 2. Телефонний довідник
phonebook = {"Іван": "0987654321", "Марія": "0677654321"}
phonebook["Олег"] = "0951234567"   # додавання
name = "Іван"
print(f"Номер {name}:", phonebook.get(name, "не знайдено"))  # пошук
del phonebook["Марія"]             # видалення
for name, phone in phonebook.items():
    print(name, "-", phone)
