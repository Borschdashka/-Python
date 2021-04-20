from itertools import count
from math import factorial

def factorial_gen(number):
    fact_num = 1
    if number == 0:
        yield f'{number}! = 1'
    for j in range(1, number + 1):
        fact_num *= j
        yield f'{j}! = {fact_num}'

for el in factorial_gen(int(input('Факториал числа: '))):
    print(el)