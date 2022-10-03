kolya = int(input('Кубик Кости: '))
vitya = int(input('Кубик владельца: '))
if kolya >= vitya:
    print(kolya - vitya)
    print('Костя платит')
else:
    print(kolya + vitya)
    print('Владелец платит')
print('Игра окончена.')
