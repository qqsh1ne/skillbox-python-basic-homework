number = float(input('Введите неотрицательное число: '))
e = 0
while number < 1:
    number *= 10
    e -= 1
while number >= 10:
    number /= 10
    e += 1
print(f'Формат плавающей точки: x = {round(number, 15)} * 10 ** {e}')
