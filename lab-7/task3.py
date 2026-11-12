# Завдання 3. Клас Book
class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def info(self):
        print(f"«{self.title}», {self.author}, {self.pages} с., {self.year} р.")

    def is_new(self):
        return self.year > 2015


books = [Book("Кобзар", "Т. Шевченко", 400, 1840),
         Book("Ворошиловград", "С. Жадан", 440, 2010),
         Book("Інтернат", "С. Жадан", 336, 2017),
         Book("Python для початківців", "О. Коваль", 250, 2022)]

print("Нові книги:")
for b in books:
    if b.is_new():
        b.info()
