def positive():
    print('Число положительное')


def negative():
    print('Число отрицательное')


def test():
    number = int(input('Введите число: '))
    if number > 0:
        positive()
    else:
        negative()


test()
