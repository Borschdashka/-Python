rating = []
while True:
    num = int(input('Введите целое число: '))
    if num == 0:
        break
    elif num == 9:
        rating.insert(0, num)
    else:
        index = 0
        for item in rating:
            if num > item:
                break
            index += 1
        rating.insert(index, num)
    print(rating)
