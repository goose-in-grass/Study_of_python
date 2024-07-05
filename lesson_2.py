class Point:
    color = "red"
    circle = 2

    def set_coords(self):
        # self - это ссылка на экземпляр класса
        print("Вызов метода set_coords" + str(self))


pt = Point()
