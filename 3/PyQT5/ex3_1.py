from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from ex2_1 import Date


# Определение класса ProductDate, наследующего от класса Date
class ProductDate(Date):
    def __init__(self, day=1, month=1, year=2000, release_year=2000):
        super().__init__(day, month, year)
        self.release_year = release_year

    def calculate_age(self):
        # Вычисление возраста товара
        current_year = 2023
        age = current_year - self.release_year
        return age

    def get_info(self):
        # Получение информации о товаре, включая год выпуска
        parent_info = super().get_info()
        return f"{parent_info}\nГод выпуска товара: {self.release_year}"

# Определение класса MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание компонента QTextEdit для вывода информации
        self.memo = QTextEdit(self)
        self.setCentralWidget(self.memo)

        # Вызов метода для обработки данных
        self.process_data()

    def process_data(self):
        # Создание объекта класса ProductDate с заданными значениями полей
        product = ProductDate(7, 7, 2022, 2010)

        # Вывод информации о товаре
        self.memo.append(product.get_info())

        # Вычисление возраста товара
        age = product.calculate_age()

        # Вывод возраста товара
        self.memo.append(f"Возраст товара: {age} лет")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


'''
# Определение класса ProductDate, наследующегося от класса Date
class ProductDate(Date):
    def __init__(self, release_year, day, month, year):
        super().__init__(day, month, year)
        self.release_year = release_year

    def get_info(self):
        return f"Дата: {self.day}.{self.month}.{self.year}\nГод выпуска товара: {self.release_year}"

    def get_product_age(self):
        current_year = 2022  # Замените на текущий год
        age = current_year - self.release_year
        return f"Возраст товара: {age} лет"

# Определение класса MainWindow, унаследованного от QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memo = QTextEdit(self)  # Создание компонента QTextEdit
        self.setCentralWidget(self.memo)  # Установка компонента QTextEdit в качестве центрального виджета

        self.process_data()

    def process_data(self):
        # Создание объекта класса Date и вывод информации о дате
        date = Date(7, 7, 2022)
        self.memo.append(date.get_info())
        self.memo.append(date.check_date())

        # Создание объекта класса ProductDate и вывод информации о дате и возрасте товара
        product_date = ProductDate(2010, 7, 7, 2022)
        self.memo.append(product_date.get_info())
        self.memo.append(product_date.get_product_age())

# Создание экземпляра QApplication
app = QApplication([])

# Создание экземпляра MainWindow
window = MainWindow()
window.show()

# Запуск главного цикла приложения
app.exec_()'''
