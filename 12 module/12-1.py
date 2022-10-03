def summa_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f'Я знаю, что сумма чисел от 1 до {n} равна {sum}')


summa_n(int(input('Введите число: ')))
