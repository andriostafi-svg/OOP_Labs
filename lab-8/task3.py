# Завдання 3. Поліморфізм
class Cat:
    def sound(self):
        return "Няв"

class Dog:
    def sound(self):
        return "Гав"

class Parrot:
    def sound(self):
        return "Привіт!"


animals = [Cat(), Dog(), Parrot()]
for a in animals:
    print(type(a).__name__, "-", a.sound())
