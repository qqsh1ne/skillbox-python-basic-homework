import random


numbers_count = int(input('Кол-во чисел в списке: '))

initial_list = [random.randint(0, 2) for _ in range(numbers_count)]
print('Список до сжатия:', initial_list)
print('Список после сжатия:', [x for x in initial_list if x > 0])