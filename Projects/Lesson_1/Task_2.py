sec = int (input ('Введите время в секундах'))
hour = sec // 3600 #время в часах
min = (sec - hour * 3600) // 60
sec = sec % 60
print (hour, ":", min, ":", sec)
