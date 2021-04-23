class Worker:
    name = None
    surname = None
    position = None
    _income = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_full_income(self):
        self._income = {'profit': self.profit, 'bonus': self.bonus}
        return self._income

developer = Position('Anton ', 'Lebedev', 'developer', 25000, 8000)
print(developer.get_full_name(), developer.get_full_income())
