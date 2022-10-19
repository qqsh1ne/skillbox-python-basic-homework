sticks_amount = int(input('Количество палок: '))
sticks = ['I' for _ in range(sticks_amount)]
throws_amount = int(input('Количество бросков: '))

for i_throw in range(throws_amount):
    start = int(input(f'Бросок {i_throw + 1}. Сбиты палки с номера ')) - 1
    end = int(input('по номер ')) - 1
    for stick in range(start, end + 1):
        sticks[stick] = '.'
print('Результат: ', *sticks, sep='')