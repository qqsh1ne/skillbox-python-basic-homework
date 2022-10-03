positive_count = 0
negative_count = 0
while True:
    review = int(input("Введите число: "))
    if review > 0:
        positive_count += 1
    elif review < 0:
        negative_count += 1
    else:
        print("Кол-во положительных чисел:", positive_count)
        print("Кол-во отрицательных чисел:", negative_count)
        break