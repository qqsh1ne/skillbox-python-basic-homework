import math


a = float(input('Введите коэффициент а, не равный нулю: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

if a != 0:
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f'Уравнение имеет два корня: \nx1 = {x1}\nx2 = {x2}')
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f'Уравнение имеет один корень: x = {x}')
    else:
        print("Корней нет")
else:
    print('Это уже не квадратное уравнение!')