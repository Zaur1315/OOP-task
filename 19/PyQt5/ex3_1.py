from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from ex2_1 import Vector


class VectorChild(Vector):
    def __init__(self, x1, x2, x3, x4, c):
        super().__init__(x1, x2, x3, x4)
        self.c = c

    def process_coordinates(self):
        self.coordinates[0] += self.c  # Увеличение первой координаты на "c"
        self.coordinates[1] += self.c  # Увеличение второй координаты на "c"
        # Нахождение произведения координат
        product = self.coordinates[0] * self.coordinates[1]
        return product


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memo = QTextEdit(self)
        self.setCentralWidget(self.memo)

        self.process_data()

    def process_data(self):
        # Создание объекта класса VectorChild с заданными координатами и "c"
        vector_child = VectorChild(1, 2, 5, 6, 2)

        # Вывод информации об объекте в компонент Memo
        self.memo.append(vector_child.get_info())

        # Обработка координат и нахождение произведения
        product = vector_child.process_coordinates()
        # Вывод произведения координат
        self.memo.append(f"Произведение: {product}")

        del vector_child  # Уничтожение объекта


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
