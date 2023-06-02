class Product:
    def __init__(self, price, quantity):
        self.field_1 = price  # Инициализация поля field1 значением price
        self.field_2 = quantity  # Инициализация поля field2 значением quantity

    def get_info(self):
        return f"Цена товара: {self.field_1}\nКоличество единиц товара: {self.field_2}"

    def calculate_total_cost(self):
        total_cost = self.field_1 * self.field_2  # Вычисление общей стоимости товара
        return total_cost


# Создание объекта класса Product с заданными значениями полей
product = Product(10, 5)

# Вывод информации о товаре
print(product.get_info())

# Вычисление общей стоимости товара
total_cost = product.calculate_total_cost()

# Вывод общей стоимости товара
print("Общая стоимость товара:", total_cost)
