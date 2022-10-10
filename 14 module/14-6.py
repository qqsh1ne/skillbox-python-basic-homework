import math

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if math.sqrt(x * x + y * y) > radius:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')