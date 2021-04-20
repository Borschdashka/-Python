f = open("to_task_2.txt", "r")
content = f.readlines()
print (len(content))
for str in content:
    str_list = str.split()
print(len(str_list))
f.close()
