number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
sum, count = 0, 0
for i in range(number_1, number_2 + 1):
    if i % number_3 == 0:
        count += 1
        sum += i
if count == 0:
    print('Нет чисел, кратных', number_3)
else:
    print(f'Среднее арифметическое чисел, кратных {number_3}: {sum / count}')