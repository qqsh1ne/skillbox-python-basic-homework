def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fib(number))
