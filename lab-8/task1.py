# Завдання 1. Працівник і Менеджер
class Worker:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        return f"{self.name}, {self.position}, {self.salary} грн"


class Manager(Worker):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department

    def info(self):   # перевизначений метод
        return f"{super().info()}, відділ: {self.department}"


print(Worker("Іван", "програміст", 30000).info())
print(Manager("Олена", "менеджер", 40000, "Продажі").info())
