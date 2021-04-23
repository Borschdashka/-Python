#через словарь
month = int(input('Введите месяц числом от 1 до 12: '))
my_dict = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for season, months in my_dict.items():
    if month in months:
        print(season)
        break