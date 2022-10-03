line = int(input('Введите кол-во рядов: '))
place = int(input('Введите кол-во сидений в ряду: '))
meters = int(input('Введите кол-во метров между рядами: '))
for i in range(line):
    print('=' * place + ' ' + '*' * meters + ' ' + '=' * place)