# создание класса

class Item:

    def __init__(self, name: str, price: float, quantity=0):
        # присвоение
        self.name = name
        self.price = price
        self.quantity = quantity

        # проверка
        assert price >= 0, f"Долбаеб, {price} цена не может быть отрицательной"
        assert quantity >= 0, f"Децел, {quantity} количество тоже"
        # assert - ключевое слово для проверки ваших ожиданий

    # name:str - Это знак ввода, проверка на правильный ввод типа данных

    # self это что-то типо обозначения для полей класса

    def calculate_total_price(self):
        return self.price * self.quantity
    # не передаем параметры в def потому что self уже содержит их (price & quantity)


item1 = Item("Phone", 100, 1)  # объект класса
item2 = Item("Laptop", 1000, 1)  # объект класса
item2.has_numpad = False

print(item1.calculate_total_price())
print(item2.calculate_total_price())
