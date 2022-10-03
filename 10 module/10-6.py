number = int(input('Введите число: '))
factorial = 1
factorial_sum = 0
for i in range(1, number + 1):
    factorial *= i
    factorial_sum += factorial
print('\nСумма факториалов равна:', factorial_sum)
