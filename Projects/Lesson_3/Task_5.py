current_sum = 0
exit_flag = False
while not exit_flag:
    input_data = input('Введите целые числа разделённые пробелом или ''q'' для выхода: ').split(' ')
    for data in input_data:
        if data == 'q':
            exit_flag = True
            break
        current_sum += int(data)
    print("Текущая сумма чисел", current_sum)