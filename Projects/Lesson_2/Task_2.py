spisok = list (input('Введите элементы списка'))
j = 0
for i in range (int(len(spisok)/2)):
    spisok[j], spisok[j+1] = spisok[j+1], spisok [j]
    j += 2
print (spisok)
