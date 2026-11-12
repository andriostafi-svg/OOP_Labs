# Завдання 2. Клас Car
class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def start(self):
        print("Двигун запущено")

    def stop(self):
        print("Двигун зупинено")

    def drive(self, km):
        self.mileage += km
        print(f"Проїхали {km} км")

    def info(self):
        print(f"{self.brand} {self.model}, {self.year} р., пробіг {self.mileage} км")


car = Car("Toyota", "Corolla", 2018, 50000)
car.info()
car.start()
car.drive(120)
car.stop()
car.info()
