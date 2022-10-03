first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
max = (first_number + second_number + abs(first_number - second_number)) / 2
print('Наибольшее число: ', max)