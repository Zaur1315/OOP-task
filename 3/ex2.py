class Date:
    def __init__(self, day=1, month=1, year=2000):
        # Конструктор по умолчанию
        self.day = day  # Инициализация поля day значением day
        self.month = month  # Инициализация поля month значением month
        self.year = year  # Инициализация поля year значением year

    def __init__(self, day, month, year):
        # Конструктор перезагрузки с параметрами
        self.day = day  # Инициализация поля day значением day
        self.month = month  # Инициализация поля month значением month
        self.year = year  # Инициализация поля year значением year

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


# Создание объекта класса Date с заданными значениями полей
date = Date(7, 7, 2022)


print('\nИз класса Date')

# Вывод информации о дате
print(date.get_info())

# Проверка совпадения номера месяца и числа дня
print(date.check_date())

# Увеличение даты на один месяц
date.increase_month()

# Вывод информации о дате после увеличения
print(date.get_info())
