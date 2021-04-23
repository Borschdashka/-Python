class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Рассчитаем, сколько необходимо асфальтового покрытия для строительства дороги')

    def result(self):
        self.weigth = float(input('Введите массу (кг) асфальта для покрытия 1 кв.м. дороги'))
        self.tickness = float(input('Введите толщину покрытия'))
        result = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Необходимо {result} кг для строительства')

road = Road(20000, 6)
road.result()