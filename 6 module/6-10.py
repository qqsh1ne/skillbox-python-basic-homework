min = 1
max = 100
count = 0
start_number = int(input('Введите загаданное число (от 1 до 100): '))
while True:
    n = (max + min) // 2
    print("Твоё число равно, больше или меньше числа", n, "?")
    if n > start_number:
        max = n - 1
    elif n < start_number:
        min = n + 1
    else:
        print('Я угадал!')
        print('За ' + str(count) + ' попыток')
        break
    count += 1