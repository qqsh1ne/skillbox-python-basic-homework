print('Ввод:')
lower_bound = int(input('Нижняя граница: '))
upper_bound = int(input('Верхняя граница: '))
step = int(input('Шаг: '))

print('Вывод: ')
print('C', '\t', 'F')

for i in range(lower_bound, upper_bound + step, step):
    if i > upper_bound:
        print(upper_bound, '\t', round(upper_bound * 1.8 + 32))
        break
    print(i, '\t', round(i * 1.8 + 32))
