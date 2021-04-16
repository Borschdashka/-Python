my_list = [2, 32, 5, 8, 6, 32, 5, 7, 8]
new_list = [el for el in my_list if my_list.count(el)==1]
print(new_list)