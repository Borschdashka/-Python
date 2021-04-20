from sys import argv

rach, hours, stav, prem, zp = argv

print("Имя скрипта: ", rach)
int(input("Введите выработку в часах", hours))
int(input("Введите ставку в час", stav))
int(input("Введите размер премии", prem))
zp = hours * stav + prem
print('Зарплата = ', zp)
