positive_prime_count = 0
for number in range(1, 11):
    id = int(input(f'Введите число {number} : '))
    if id % 2 == 0 and id > 0:
        positive_prime_count += 1
print(positive_prime_count, 'чисел являются четными и положительными')
