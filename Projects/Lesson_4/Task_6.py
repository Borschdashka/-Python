from itertools import count, cycle

print('Введите целое число. Нажмите Enter. Вы получите следующее целое число. Для выхода нажмите q')
for el in count(int(input('Введите первое число: '))):
    print(el, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter, для выхода',
      ' из программы нажмите q')
my_list = input('Введите элементы списка, разделяя их пробелом: ').split()
iter_ = cycle(my_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()
