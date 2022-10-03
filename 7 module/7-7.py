start = int(input('Введите координату начала отрезка: '))
end = int(input('Введите координату конца отрезка: '))
number_sum, number_count = 0, 0
for number in range(start, end + 1):
    if number % 3 == 0:
        number_sum += number
        number_count += 1
print('Cреднее арифметическое чисел, кратных 3 из отрезка', start, 'и', end, ':', number_sum / number_count)
