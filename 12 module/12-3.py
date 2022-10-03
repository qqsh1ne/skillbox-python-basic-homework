def get_digits_sum():
    number = int(input('Введите число: '))
    sum_number = 0
    while number > 0:
        sum_number += number % 10
        number = number // 10
    print(f'Сумма цифр числа равна {sum_number}')


def get_max_number():
    number = int(input('Введите число: '))
    max_number = number % 10
    while number > 0:
        number = number // 10
        if max_number < number % 10:
            max_number = number % 10
    print(f'Максимальная цифра в числе равна {max_number}')


def get_min_number():
    number = int(input('Введите число: '))
    min_number = number % 10
    while number > 0:
        number = number // 10
        if number == 0:
            break
        if min_number > number % 10:
            min_number = number % 10
    print(f'Минимальная цифра в числе равна {min_number}')


def calculate():
    while True:
        act = int(input(
            'Выберите действие (0 - вывести сумму цифр числа, 1 - вывести максимальную цифру числа, 2 - вывести минимальную цифру числа): '))
        if act == 0:
            get_digits_sum()
            print('\n')
        elif act == 1:
            get_max_number()
            print('\n')
        else:
            get_min_number()
            print('\n')


calculate()
