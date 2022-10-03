length = 115
v = int(input('Введите скорость: '))
t = int(input('Введите время: '))
distance_covered = v * t % length
print('Номер километра следующего круга: ', distance_covered)