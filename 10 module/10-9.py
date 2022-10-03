height = int(input('Введите высоту пирамидки: '))
count = 1
for i in range(0, height + 1):
    print('\t' * (height - i), end='')
    for j in range(i):
        print(count, end='')
        print('\t' * 2, end='')
        count += 2
    print()
