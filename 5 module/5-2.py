number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

if (number_1 > number_2 and number_1 > number_3):
    print(number_1)
elif (number_2 > number_1 and number_2 > number_3):
    print(number_2)
else:
    print(number_3)