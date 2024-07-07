#  Магический метод __new__

# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("Вызов __new__" + str(cls))  # должен возвращать адресс нового созданного объекта
#         return super().__new__(cls)
#
#     # cls ссылается на текущий класс
#     # в данном случае на класс Point
#
#     def __init__(self, x=0, y=0):
#         print("вызов __init__ для " + str(self))
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# print(pt)


# Реализуем паттерн singleton

class DataBase: # Идея в том, что мы можем создать только одну базу данных
# Строчки с 25 по 38 определяют этот паттерн
    __instance = None # ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        DataBase.__instance = None

    def connect(self):
        print(f"соединение с БД:  {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие соединения с БД")

    def read(self):
        return "Данные из БД"

    def write(self, data):
        print(f"Запись в БД {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))
