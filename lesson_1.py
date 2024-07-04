# создание класса

class Item:
    pay_rate = 0.8  # after 20% discount

    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # проверка
        assert price >= 0, f"Долбаеб, {price} цена не может быть отрицательной"
        assert quantity >= 0, f"Децел, {quantity} количество тоже"
        # assert - ключевое слово для проверки ваших ожиданий

        # присвоение
        self.name = name
        self.price = price
        self.quantity = quantity


        #
        Item.all.append(self)

    # name:str - Это знак ввода, проверка на правильный ввод типа данных

    # self это что-то типо обозначения для полей класса

    def calculate_total_price(self):
        return self.price * self.quantity

    # не передаем параметры в def потому что self уже содержит их (price & quantity)

    def apply_discount(self):
        self.price = self.price * self.pay_rate


#TODO: разобраться с функцией __repr__ and self


    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)