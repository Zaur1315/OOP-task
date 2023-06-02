from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class Date:
    def __init__(self, day=1, month=1, year=2000):
        # Конструктор по умолчанию или перезагрузка с параметрами
        self.day = day
        self.month = month
        self.year = year

    def __del__(self):
        # Деструктор для освобождения памяти
        print("Объект удален")

    def check_date(self):
        # Функция-метод 1 обработки данных: определение совпадения номера месяца и числа дня
        if self.month == self.day:
            return "Номер месяца и число дня совпадают"
        else:
            return "Номер месяца и число дня не совпадают"

    def increase_month(self):
        # Функция-метод 2 обработки данных: увеличение даты на один месяц
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

    def get_info(self):
        # Функция формирования строки информации об объекте
        return f"Дата: {self.day}.{self.month}.{self.year}"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memo = QTextEdit(self)
        self.setCentralWidget(self.memo)

        self.process_data()

    def process_data(self):
        # Создание объекта класса Date с заданными значениями полей
        date = Date(7, 7, 2022)

        # Вывод информации о дате
        self.memo.append(date.get_info())

        # Проверка совпадения номера месяца и числа дня
        self.memo.append(date.check_date())

        # Увеличение даты на один месяц
        date.increase_month()

        # Вывод информации о дате после увеличения
        self.memo.append(date.get_info())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
