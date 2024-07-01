# создание класса

class Item:
    pay_rate = 0.8  # after 20% discount

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

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)  # объект класса
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
