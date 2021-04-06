my_list = input('Введите список, элементы разделяем пробелом: ').split(' ')
for enum in enumerate(my_list, 1):
    print(enum[0], enum[1][:10])