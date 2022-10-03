height = int(input('Введите высоту пирамидки: '))
count = 1
for i in range(0, height):
    for j in range(1, height - i):
        print(' ', end='')
    print(count * '#', end='')
    count += 2
    print()
