from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class Point:
    def __init__(self, x, y):
        self.field1 = x  # Инициализация поля field1 значением x
        self.field2 = y  # Инициализация поля field2 значением y

    def get_info(self):
        return f"Point coordinates: ({self.field1}, {self.field2})"

    def calculate_perimeter(self):
        # Вычисление периметра прямоугольника
        perimeter = 2 * (self.field1 + self.field2)
        return perimeter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memo = QTextEdit(self)
        self.setCentralWidget(self.memo)

        self.process_data()

    def process_data(self):
        # Создание объекта first_point с координатами (3, 4)
        first_point = Point(3, 4)
        # Создание объекта second_point с координатами (5, 2)
        second_point = Point(5, 2)

        # Вывод информации о первой точке
        self.memo.append(first_point.get_info())
        # Вывод информации о второй точке
        self.memo.append(second_point.get_info())

        # Вычисление периметра для первой точки
        first_perimeter = first_point.calculate_perimeter()
        # Вычисление периметра для второй точки
        second_perimeter = second_point.calculate_perimeter()

        # Вывод периметра первого прямоугольника
        self.memo.append(f"Perimeter of rectangle 1: {first_perimeter}")
        # Вывод периметра второго прямоугольника
        self.memo.append(f"Perimeter of rectangle 2: {second_perimeter}")


if __name__ == '__main__':
    app = QApplication([])  # Создание объекта приложения
    window = MainWindow()  # Создание объекта главного окна
    window.show()  # Отображение главного окна
    app.exec_()  # Запуск основного цикла приложения
