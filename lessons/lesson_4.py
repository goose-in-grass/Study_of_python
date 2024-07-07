#  Магический метод __new__

class Point:
    def __new__(cls, *args, **kwargs):
        print("Вызов __new__" + str(cls))  # должен возвращать адресс нового созданного объекта
        return super().__new__(cls)

    # cls ссылается на текущий класс
    # в данном случае на класс Point

    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)