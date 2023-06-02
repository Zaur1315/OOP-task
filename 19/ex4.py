from ex3 import VectorChild


class VectorGrandchild(VectorChild):
    def __init__(self, x1, y1, x2, y2, a, b):
        # Вызываем конструктор родительского класса VectorChild и передаем значения x1, y1, x2, y2 и 0
        super().__init__(x1, y1, x2, y2, 0)
        self.a = a  # Инициализируем поле a значением, переданным в конструктор
        self.b = b  # Инициализируем поле b значением, переданным в конструктор

    def calculate_area(self):
        # Находим длины сторон параллелограмма
        side1 = abs(self.coordinates[2] - self.coordinates[0])
        side2 = abs(self.coordinates[3] - self.coordinates[1] + self.b)

        # Вычисляем площадь параллелограмма
        area = side1 * side2
        return area

    def get_info(self):
        # Формируем строки с координатами
        info = "Координаты первого вектора: [{}, {}]\n".format(
            self.coordinates[0], self.coordinates[1])
        info += "Координаты второго вектора: [{}, {}]\n".format(
            self.coordinates[2], self.coordinates[3])
        # Добавляем строку с информацией о смещении по оси Ox
        info += "Смещение по оси Ox: {}\n".format(self.a)
        # Добавляем строку с информацией о смещении по оси Oy
        info += "Смещение по оси Oy: {}\n".format(self.b)
        return info


vector_grandchild = VectorGrandchild(1, 2, 5, 6, 3, 2)
# Вывод информации об объекте
print(vector_grandchild.get_info())
# Вычисление площади параллелограмма
area = vector_grandchild.calculate_area()
# Вывод площади
print("Площадь параллелограмма:", area)
