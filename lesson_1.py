# создание класса

class Item:
    def calculate_toatal_price(self, x, y):
        return x * y






item1 = Item()  #объект класса
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_toatal_price(item1.price, item1.quantity))

item2 = Item()  #объект класса
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_toatal_price(item2.price, item2.quantity))
