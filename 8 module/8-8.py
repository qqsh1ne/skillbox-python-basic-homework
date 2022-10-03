n = int(input('Введите число: '))
series_sum = 0
for number in range(n + 1):
    series_sum += ((-1) ** number) * (1 / (2 ** number))
print(f'Сумма ряда равна: {series_sum}')