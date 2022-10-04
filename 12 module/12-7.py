def min_number():
    number_1 = int(input("Введите первое число: "))
    number_2 = int(input("Введите второе число: "))
    min = round(((number_1 + number_2) - abs(number_1 - number_2)) / 2)
    print("Минимальное число:", min)


min_number()
