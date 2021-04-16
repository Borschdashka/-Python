from functools import reduce
def first_list(num_1, num_2):
    return num_1 * num_2

new_list = [num for num in range(100, 1001, 2)]
print(f"List\n{new_list}\nПроизведение элементов списка\n{reduce(first_list, new_list)}")
print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))