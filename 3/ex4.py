from ex3 import ProductDate
from datetime import datetime


class MedicineDate(ProductDate):
    def __init__(self, name, day, month, year, company):
        # Конструктор класса-потомка с полями класса-родителя и дополнительными полями
        super().__init__(day, month, year)
        self.name = name
        self.company = company

    def get_days_since_manufacture(self):
        # Функция-метод обработки данных объекта класса-потомка
        # Рассчитываем количество прошедших дней от изготовления лекарства
        # (предполагая, что текущая дата - 7 июня 2022)
        current_day = datetime.now().day
        current_month = datetime.now().month
        current_year = datetime.now().year
        days = (current_year - self.year) * 365 + \
            (current_month - self.month) * 30 + (current_day - self.day)
        return f"Прошло дней от изготовления лекарства: {days}"

    def get_info(self):
        # Переопределяем функцию форматирования строки информации об объекте для класса-потомка
        return f"Наименование лекарства: {self.name}\n{super().get_info()}\nФирма: {self.company}"


# Создание объектов классов и вывод информации


# Объект класса-потомка
medicine_date = MedicineDate("Аспирин", 1, 1, 2022, "Фармаком")
print("\nИз класса MedicineDate ( Наследумый от ProductDate )")
print(medicine_date.get_info())
print(medicine_date.get_days_since_manufacture())
