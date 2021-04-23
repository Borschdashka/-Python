num_str = input ('ведите целое положительное число: ')
num = int (num_str)
max_digit = 0
while num > 0:
    next_digit = num % 10
    max_digit = max (next_digit, max_digit)
    num //= 10
print (max_digit)


