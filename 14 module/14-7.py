first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print(f'Годы от {first_year} до {second_year} с тремя одинаковыми цифрами:')
for year in range(first_year, second_year + 1):
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp = year
    while temp > 0:
        digits[temp % 10] += 1
        temp //= 10
    for digit in digits:
        if digit == 3:
            print(year)
            break
