depth = int(input('Введите глубину ямы: '))
for i in range(1, depth + 1):
    for j in range(i):
        print(depth - j, end='')
    print('.' * ((depth - i) * 2), end='')
    for j in range(i, 0, -1):
        print(depth - j + 1, end='')
    print()
