f = open("to_task_1.txt", "w")
while True:
    str = input('Введите очередную строку')
    if len(str) == 0:
        print('Конец программы')
        break
f.close()
