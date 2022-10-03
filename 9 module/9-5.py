x = 8
y = 10
vertical_size = 20
horizontal_size = 15
while True:
    print(f'[Программа]: Марсоход находится на позиции {x}, {y}, введите команду: ')
    command = input('[Оператор]: ')
    if command == 'W' and y != vertical_size:
        y += 1
    elif command == 'S' and y != 0:
        y -= 1
    elif command == 'A' and x != 0:
        x -= 1
    elif command == 'D' and x != horizontal_size:
        x += 1
    else:
        print('Неверная команда')
