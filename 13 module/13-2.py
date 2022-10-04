def get_max_number(x, y):
    return ((x + y) + abs(x - y)) / 2


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

print(f'Наибольшее число: {get_max_number(get_max_number(number_1, number_2), number_3)}')