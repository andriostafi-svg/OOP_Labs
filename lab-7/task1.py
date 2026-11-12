# Завдання 1. Клас Student
class Student:
    def __init__(self, name, group, rating):
        self.name = name
        self.group = group
        self.rating = rating

    def info(self):
        print(f"{self.name}, {self.group}, рейтинг: {self.rating}")

    def set_rating(self, rating):
        self.rating = rating


students = [Student("Андрій", "ПЦТ-31", 85),
            Student("Марія", "ПЦТ-31", 92),
            Student("Олег", "ПЦТ-31", 78)]
students[2].set_rating(88)   # змінюємо рейтинг

students.sort(key=lambda s: s.rating, reverse=True)
for s in students:
    s.info()
