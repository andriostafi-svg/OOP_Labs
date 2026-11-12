# Завдання 2. Транспорт і Автомобіль
class Transport:
    def move(self):
        return "Рух транспортного засобу"


class Car(Transport):
    def move(self):   # перевизначений метод
        return "Автомобіль рухається дорогою"


print(Transport().move())
print(Car().move())
