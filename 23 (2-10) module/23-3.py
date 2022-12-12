import random


MAX_NUMBER = 777
sum_num = 0
file = open('out_file.txt', 'w', encoding='utf8')
file.close()
file = open('out_file.txt', 'a', encoding='utf8')

while True:
    number = 0
    try:
        number = int(input('Введите число: '))
    except ValueError:
        print('Введите корректное целое число!')
        continue
    except Exception as e:
        print(e)
        continue

    sum_num += number
    if sum_num >= MAX_NUMBER:
        file.write(str(number) + '\n')
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
        exit()

    if random.randint(1, 13) == 1:
        file.write(str(number) + '\n')
    else:
        try:
            rnd_exception = random.randint(1, 3)
            if rnd_exception == 1:
                raise IndexError('Индекс на границ элемента.')
            elif rnd_exception == 2:
                raise ArithmeticError('Арифметическая ошибка.')
            elif rnd_exception == 3:
                raise ZeroDivisionError('Деление на ноль.')
        except Exception as e:
            print(e)
        break
