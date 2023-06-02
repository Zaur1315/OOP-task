from ex2 import Vector


class VectorChild(Vector):
    # Конструктор перезагрузки с параметрами
    def __init__(self, x1, x2, x3, x4, c):
        super().__init__(x1, x2, x3, x4)
        self.c = c

    # Увеличение координат на "c"
    def process_coordinates(self):
        # Увеличение координат на "c"
        self.coordinates[0] += self.c
        self.coordinates[1] += self.c
        # Нахождение произведения координат
        product = self.coordinates[0] * self.coordinates[1]
        return product


# Создание объекта класса VectorChild с заданными координатами и "c"
vector_child = VectorChild(1, 2, 5, 6, 2)

# Вывод информации об объекте
print(vector_child.get_info())

# Обработка координат и нахождение произведения
product = vector_child.process_coordinates()

# Вывод произведения координат
print("Произведение:", product)  # Вывод произведения координат
