def scan():
    x = float(input('Введите координату Х: '))
    y = float(input('Введите координату Y: '))

    if abs(x) <= 1 and abs(y) <= 1:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


scan()
