class Point:
    # Определение конструктора
    def __init__(self, x, y):
        self.field1 = x  # Инициализация поля field1 значением x
        self.field2 = y  # Инициализация поля field2 значением y

    # Функция формирования строки с информацией об объекте
    def get_info(self):
        # Формирование строки с информацией о координатах точки
        return f"Point coordinates: ({self.field1}, {self.field2})"

    # Функция обработки значений полей объекта
    def calculate_perimeter(self):
        # Вычисление периметра прямоугольника
        perimeter = 2 * (self.field1 + self.field2)
        return perimeter



# Создание экземпляров объекта
first_point = Point(3, 4)  
second_point = Point(5, 2)

# Вывод информации об объектах
print(first_point.get_info())
print(second_point.get_info())


# Вычисление периметра прямоугольника для каждого объекта
first_perimeter = first_point.calculate_perimeter()
second_perimeter = second_point.calculate_perimeter()

# Вывод результатов
print("Perimeter of rectangle 1:", first_perimeter)
print("Perimeter of rectangle 2:", second_perimeter)
