class Stationery:
    def __init__(self, title):
        self.__title = title
    def draw(self):
        print("Запуск отрисовки", self.__title)

class Pen(Stationery):
    def __init__(self):
        Stationery.__init__(self, "ручка")

class Pencil(Stationery):
    def __init__(self):
        Stationery.__init__(self, "карандаш")
    def draw(self):
        super().draw()
        print("Дополнительные действия для отрисовки карандашом")

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()
