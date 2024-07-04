class Point:
    color = "red"
    circle = 2

    def set_coords(self):
        #self - это ссылка на экземпляр класса
        print("Вызов метода set_coords" + str(self))

# если мы объявляем метод внутри класса и хотим его использовать через объект класса,
# то нужно использовать self, как ссылку

pt = Point()