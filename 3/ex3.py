from ex2 import Date
from datetime import datetime


class ProductDate(Date):
    def __init__(self, day=1, month=1, year=2000, release_year=2000):
        super().__init__(day, month, year)
        # Вызов конструктора родительского класса и передача параметров day, month, year
        # Инициализация поля release_year значением release_year
        self.release_year = release_year

    def calculate_age(self):
        current_year = datetime.now().year
        age = current_year - self.release_year  # Вычисление возраста
        return age

    def get_info(self):
        parent_info = super().get_info()  # Вызов метода get_info родительского класса
        return f"{parent_info}\nГод выпуска товара: {self.release_year}"


# Создание объекта класса ProductDate с заданными значениями полей
product = ProductDate(7, 7, 2022, 2010)

print('\nИз класса ProductDate ( Наследуемый от Date )')

# Вывод информации о товаре
print(product.get_info())

# Вычисление возраста товара
age = product.calculate_age()
print(f"Возраст товара: {age} лет")
