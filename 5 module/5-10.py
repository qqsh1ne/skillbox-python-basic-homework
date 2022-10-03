time = int(input("Введите время в часах: "))
if (0 <= time < 8) or (10 <= time < 12) or (14 <= time < 15) or (18 <= time < 20) or (22 <= time < 24):
    print("Посылку получить нельзя.")
else:
    print("Посылку получить можно.")