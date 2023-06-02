from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from ex3_1 import VectorChild


class VectorGrandchild(VectorChild):
    def __init__(self, x1, y1, x2, y2, a, b):
        super().__init__(x1, y1, x2, y2, 0)
        self.a = a  # Инициализация поля a значением, переданным в конструктор
        self.b = b  # Инициализация поля b значением, переданным в конструктор

    def calculate_area(self):
        # Вычисление длины первой стороны
        side1 = abs(self.coordinates[2] - self.coordinates[0])
        # Вычисление длины второй стороны с учетом смещения
        side2 = abs(self.coordinates[3] - self.coordinates[1] + self.b)
        area = side1 * side2  # Вычисление площади параллелограмма
        return area

    def get_info(self):
        info = "<i>Координаты первого вектора:</i> [{}, {}]<br>".format(
            self.coordinates[0], self.coordinates[1])  # Формирование строки с координатами первого вектора
        info += "<i>Координаты второго вектора:</i> [{}, {}]<br>".format(
            self.coordinates[2], self.coordinates[3])  # Добавление строки с координатами второго вектора
        # Добавление строки с информацией о смещении по оси Ox
        info += "Смещение по оси Ox: {}\n".format(self.a)
        # Добавление строки с информацией о смещении по оси Oy
        info += "Смещение по оси Oy: {}\n".format(self.b)
        return info


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memo = QTextEdit(self)
        self.setCentralWidget(self.memo)

        self.process_data()

    def process_data(self):
        # Создание объекта VectorGrandchild
        vector_grandchild = VectorGrandchild(1, 2, 5, 6, 3, 2)
        # Вывод информации об объекте
        self.memo.append(vector_grandchild.get_info())
        area = vector_grandchild.calculate_area()  # Вычисление площади параллелограмма
        # Вывод площади параллелограмма
        self.memo.append(f"Площадь параллелограмма: {area}")


if __name__ == '__main__':
    app = QApplication([])  # Создание объекта приложения
    window = MainWindow()  # Создание объекта главного окна
    window.show()  # Отображение главного окна
    app.exec_()  # Запуск основного цикла приложения
