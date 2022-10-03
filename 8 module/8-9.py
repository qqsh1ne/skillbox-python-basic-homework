x = int(input('Введите число X: '))
numerator, denominator = 1, 1
for number in range(1, 7):
    numerator *= (x - (2 ** number - 1))
    denominator *= (x - 2 ** number)
if denominator == 0:
    print('Ошибка деления на ноль!')
else:
    print('Результат:', numerator / denominator)
