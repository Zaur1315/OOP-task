class Vector:
    # Конструктор по умолчанию
    def __init__(self):
        # Поля: координаты вектора на плоскости (x1, x2, x3, x4)
        self.coordinates = [0, 0, 0, 0]

    # Конструктор перезагрузки с параметрами
    def __init__(self, x1, x2, x3, x4):
        self.coordinates = [x1, x2, x3, x4]

    # Деструктор для освобождения памяти
    def __del__(self):
        print("Объект уничтожен.")

    # Функция-метод 1 обработки данных: вычисление координат середины вектора
    def calculate_midpoint(self):
        mid_x = (self.coordinates[0] + self.coordinates[2]) / 2
        mid_y = (self.coordinates[1] + self.coordinates[3]) / 2
        return mid_x, mid_y

    # Функция-метод 2 обработки данных: вычисление площади прямоугольного треугольника,
    def calculate_triangle_area(self):
        # образованного вектором и прямыми параллельными осям OX и OY
        base = abs(self.coordinates[2] - self.coordinates[0])
        height = abs(self.coordinates[3] - self.coordinates[1])
        area = (base * height) / 2
        return area

    # Функция формирования строки информации об объекте
    def get_info(self):
        return f"Координаты Вектора: {self.coordinates}"


# Создание объекта с использованием конструктора перезагрузки
vector = Vector(1, 2, 5, 6)

# Вывод информации об объекте
print(vector.get_info())

# Вычисление координат середины вектора
mid_x, mid_y = vector.calculate_midpoint()
print("Координаты Середины Вектора:", mid_x, mid_y)

# Вычисление площади прямоугольного треугольника
triangle_area = vector.calculate_triangle_area()
print("Площадь треугольника:", triangle_area)

# Уничтожение объекта
del vector  # Выводит: Объект уничтожен.
