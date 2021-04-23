class Car:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return 'Машина поехала'
    def stop(self):
        return 'Машина остановилась'
    def turn(self, direction):
        return 'Машина повернула ' + direction

class TownCar(Car):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

Renault = TownCar('Renault', 60, 'белый')
print(Renault.name, Renault.color, Renault.speed, Renault.is_police)
print(Renault.go(), Renault.turn('в Деревню Калиново'), Renault.stop())
sport = SportCar('Ferrari', 180, 'красный')
work1 = WorkCar('Lada', 90, 'баклажан', True)
work2 = WorkCar('ZAZ', 90, 'зеленый', False)
police = PoliceCar('Audi', 180, 'синий')