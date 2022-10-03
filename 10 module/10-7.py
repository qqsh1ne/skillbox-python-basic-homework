n = int(input('Введите кол-во чисел: '))
max_sum = -1
max_number = 0
for i in range(n):
    number = int(input('Введите число: '))
    number_sum = 0
    temp = number
    while temp > 0:
        number_sum += temp % 10
        temp //= 10
    if number_sum > max_sum:
        max_sum = number_sum
        max_number = number
print(f'Наибольшее число по сумме цифр {max_number} \nСумма цифр: {max_sum}')