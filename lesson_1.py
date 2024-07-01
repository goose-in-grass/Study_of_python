# создание класса

class Item:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    # self это что-то типо обозначения для полей класса

    def calculate_total_price(self):
        return self.price * self.quantity
    # не передаем параметры в def потому что self уже содержит их
    # (price & quantity)


item1 = Item("Phone", 100, 1)  # объект класса
item2 = Item("Laptop", 1000, 3)  # объект класса
item2.has_numpad = False

print(item1.calculate_total_price())
print(item2.calculate_total_price())
