import math

count = 0
start_number = int(input('Введите загаданное число: '))
current_number = math.inf
while current_number != start_number:
    count += 1
    current_number = int(input("Введите число: "))
    if current_number > start_number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif current_number < start_number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
print('Вы угадали! Число попыток:', count)