
def delen(a, b):
    return a / b


a = float(input('Введите делимое'))
while True:
    b = float(input('Введите делитель'))
    if b == 0:
        print("На 0 делить нельзя!")
        continue
    print(a, '/', b, '=', delen(a, b))
    break
