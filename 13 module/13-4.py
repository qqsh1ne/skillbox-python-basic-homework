number = input('Введите число в экспотенциальной форме: ').lower()
m, e = '', ''
is_on_mantissa = True

for digit in number:
    if digit == 'e':
        is_on_mantissa = False
    elif is_on_mantissa:
        m += digit
    else:
        e += digit

print('Мантисса: ', m)
print('Порядок числа: ', e)