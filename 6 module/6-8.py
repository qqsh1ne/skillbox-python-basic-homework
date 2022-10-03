import math

X = int(input("Введите сумму вклада:" ))
P = int(input("Введите проценты по вкладу:" ))
Y = int(input("Введите желаемую сумму вклада:" ))
years = 0
while X < Y:
    X += math.trunc(X / 100 * P)
    years += 1
print('Пройдет ' + str(years) + ' лет')