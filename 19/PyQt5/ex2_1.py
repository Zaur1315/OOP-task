from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class Vector:
    def __init__(self, x1, x2, x3, x4):
        self.coordinates = [x1, x2, x3, x4]

    def __del__(self):
        # Комментарий: Деструктор класса, выводит сообщение об уничтожении объекта
        print("Object destroyed.")

    def calculate_midpoint(self):
        # Комментарий: Вычисление координаты x середины вектора
        mid_x = (self.coordinates[0] + self.coordinates[2]) / 2
        # Комментарий: Вычисление координаты y середины вектора
        mid_y = (self.coordinates[1] + self.coordinates[3]) / 2
        return mid_x, mid_y

    def calculate_triangle_area(self):
        # Комментарий: Вычисление длины основания треугольника
        base = abs(self.coordinates[2] - self.coordinates[0])
        # Комментарий: Вычисление высоты треугольника
        height = abs(self.coordinates[3] - self.coordinates[1])
        # Комментарий: Вычисление площади прямоугольного треугольника
        area = (base * height) / 2
        return area

    def get_info(self):
        # Комментарий: Формирование строки с информацией об объекте
        return f"Vector coordinates: {self.coordinates}"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memo = QTextEdit(self)
        self.setCentralWidget(self.memo)

        self.process_data()

    def process_data(self):
        # Комментарий: Создание объекта класса Vector с заданными координатами
        vector = Vector(1, 2, 5, 6)

        # Комментарий: Вывод информации об объекте в компонент Memo
        self.memo.append(vector.get_info())

        # Комментарий: Вычисление координат середины вектора
        mid_x, mid_y = vector.calculate_midpoint()
        # Комментарий: Вывод координат середины вектора
        self.memo.append(f"Midpoint coordinates: {mid_x}, {mid_y}")

        # Комментарий: Вычисление площади прямоугольного треугольника
        triangle_area = vector.calculate_triangle_area()
        # Комментарий: Вывод площади прямоугольного треугольника
        self.memo.append(f"Triangle area: {triangle_area}")

        del vector  # Комментарий: Уничтожение объекта


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
