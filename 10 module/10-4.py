length = int(input('Введите длину квадрата: '))
print()

for i in range(length):
    for j in range(length):
        if j == i or j == -i + length - 1:
            print('^', end='')
        else:
            print(' ', end='')
    print('')
