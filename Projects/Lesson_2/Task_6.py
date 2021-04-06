goods = []
analytics = {"название": [], "цена": [], "количество": [], "ед": []}

for i in range(1, 4):
    name = str(input("Введите название товара: "))
    price = int(input("Введите цену товара: "))
    quantity = int(input("Введите кол-во товара: "))
    measure = str(input("Введите ед измерения: "))
    goods.append((i, {"название": name, "цена": price, "количество": quantity, "ед": measure}))

    analytics.get("название").append(name)
    analytics.get("цена").append(price)
    analytics.get("количество").append(quantity)
    analytics.get("ед").append(measure)

print(goods)
print(analytics)