# Инициализатор __init__ и финализатор __del__
# Магические методы

class Point:
    color = "red"
    circle = 2

    def __init__(self, x=0, y=0):
        print("вызов")
        self.x = x
        self.y = y

    def __del__(self):
        print("удаление экземпляра" + str(self))

    def Set_coords(self, x, y):
        self.x = x
        self.y = y

    def Get_coords(self):
        return self.x, self.y


pt = Point(2, 3)
print(pt.__dict__)

# пока на объект есть хотя бы одна внешняя ссылка, то он не удаляется
