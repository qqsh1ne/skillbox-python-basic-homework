mileage = int(input('Введите пробег: '))
day = int(input('Введите сегодняшнее число: '))
if mileage // 100 + mileage % 100 // 10 + mileage % 10 > day:
    print('Сброс')
    mileage = 0
    print('Пробег:', mileage)
else:
    print('Сегодня не сломался')
    print('Пробег:', mileage)
