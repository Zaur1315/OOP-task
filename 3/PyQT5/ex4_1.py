from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class Date:
    def __init__(self, day=1, month=1, year=2000):
        # Конструктор по умолчанию или перезагрузка с параметрами
        self.day = day
        self.month = month
        self.year = year

    def get_info(self):
        # Функция форматирования строки информации об объекте
        return f"Дата: {self.day}.{self.month}.{self.year}"


class MedicineDate(Date):
    def __init__(self, name, day, month, year, company):
        # Конструктор класса-потомка с полями класса-родителя и дополнительными полями
        super().__init__(day, month, year)
        self.name = name
        self.company = company

    def get_days_since_manufacture(self):
        # Функция-метод обработки данных объекта класса-потомка
        # Рассчитываем количество прошедших дней от изготовления лекарства
        # (предполагая, что текущая дата - 7 июня 2022)
        current_day = 7
        current_month = 6
        current_year = 2022
        days = (current_year - self.year) * 365 + \
            (current_month - self.month) * 30 + (current_day - self.day)
        return f"Прошло дней от изготовления лекарства: {days}"

    def get_info(self):
        # Переопределяем функцию форматирования строки информации об объекте для класса-потомка
        return f"Наименование лекарства: {self.name}\n{super().get_info()}\nФирма: {self.company}"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memo = QTextEdit(self)
        self.setCentralWidget(self.memo)

        self.process_data()

    def process_data(self):
        # Создание объектов классов и вывод информации

        # Объект класса-родителя
        date = Date(7, 7, 2022)
        self.memo.append(date.get_info())

        # Объект класса-потомка
        medicine_date = MedicineDate("Аспирин", 1, 1, 2022, "Фармаком")
        self.memo.append(medicine_date.get_info())
        self.memo.append(medicine_date.get_days_since_manufacture())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
