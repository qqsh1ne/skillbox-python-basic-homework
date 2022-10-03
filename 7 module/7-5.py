N = int(input('Введите число: '))
factorial = 1
for number in range(1, N + 1):
    factorial *= number
print('Факториал числа', N, 'равен:', factorial)