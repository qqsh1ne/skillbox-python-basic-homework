first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')

first_string_length = len(first_string)
second_string_length = len(second_string)

if first_string == second_string:
    print('Строки одинаковые.')
    exit()

if first_string_length != second_string_length:
    print('Строки имеют разную длину.')
    exit()

shift = 1
for i in range(first_string_length - 1):
    second_string = ''.join([second_string[-1], second_string[:-1]])
    if first_string == second_string:
        print(f'Первая строка получается из второй со сдвигом {shift}.')
        exit()
    shift += 1
print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


