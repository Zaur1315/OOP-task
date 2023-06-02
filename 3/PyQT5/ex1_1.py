from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class Date:
    def __init__(self, day=1, month=1, year=2000):
        # Конструктор по умолчанию для инициализации объекта
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        # Функция формирования строки с информацией об объекте
        return f"Date: {self.day}/{self.month}/{self.year}"

    def check_date(self):
        # Функция-метод 1 обработки данных: Определить, совпадают ли номер месяца и число дня
        return self.month == self.day

    def increment_month(self):
        # Функция-метод 2 обработки данных: Увеличить дату на один месяц
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memo = QTextEdit(self)
        self.setCentralWidget(self.memo)

        self.process_data()

    def process_data(self):
        # Создание объекта с заданными значениями
        date = Date(25, 12, 2022)
        self.memo.append(str(date))  # Вывод информации об объекте

        is_same = date.check_date()  # Проверка совпадения номера месяца и числа дня
        self.memo.append(f"Is same: {is_same}")

        date.increment_month()  # Увеличение даты на один месяц
        self.memo.append(str(date))  # Вывод измененной даты


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
