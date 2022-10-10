def get_row_sum(x, precision):
    summa, factorial, result = 1, 1, 1
    while abs(summa) > precision:
        summa *= -1 * x * x / (factorial * (factorial + 1))
        factorial += 2
        result += summa
    return result


print('Сумма ряда = ', get_row_sum(float(input('Введите число: ')), float(input('Введите точность: '))))
