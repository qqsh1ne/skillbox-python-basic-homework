import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


line_number = 0
my_list = []
with open('coordinates.txt', 'r', encoding='utf-8') as coordinate_file:
    for row in coordinate_file:
        line_number += 1
        num_list = row.split()
        if len(num_list) != 2:
            raise Exception(f'Ошибка: В строке {line_number} не две координаты.')
        try:
            res1 = f(int(num_list[0]), int(num_list[1]))
            print(str(line_number), 'res1 =', res1)
            try:
                res2 = f2(int(num_list[0]), int(num_list[1]))
                print(str(line_number), 'res2 =', res2)
                number = random.randint(0, 100)
                my_list.append(sorted([number, res1, res2]))
            except ZeroDivisionError:
                print(f'В строке {line_number} попытка деления на 0.')
            except Exception:
                print(f'Строка {line_number} содержит неверные данные')
        except ZeroDivisionError:
            print(f'В строке {line_number} попытка деления на 0.')
        except Exception:
            print(f'Строка {line_number} содержит не  данные')
    sorted_data = sorted(my_list)
    with open('result.txt', 'w', encoding='utf8') as save_file:
        for row in sorted_data:
            save_file.write('\t'.join([str(item) for item in row]) + '\n')
