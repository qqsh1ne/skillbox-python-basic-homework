numbers_quantity = int(input('Введите кол-во чисел: '))
count = 0

for i in range(1, numbers_quantity + 1):
    is_prime = True
    number = int(input('Введите число: '))
    for j in range(2, number):
        if number % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print(f'Кол-во простых чисел в последовательности: {count}')
