def nod(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    print(f'Наибольший общий делитель двух чисел = {number1 + number2}')


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

nod(number_1, number_2)
