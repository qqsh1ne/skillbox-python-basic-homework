chair_1 = int(input('Введите стоимость 1 стула: '))
chair_2 = int(input('Введите стоимость 2 стула: '))
chair_3 = int(input('Введите стоимость 3 стула: '))
sum = chair_1 + chair_2 + chair_3
if sum > 10000:
    sum = sum - sum / 100 * 10
    print('Стоимость со скидкой:', sum)
else:
    print('Стоимость:', sum)
