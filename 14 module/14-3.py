def get_digits_sum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


def get_number_length(number):
    length = 0
    while number > 0:
        length += 1
        number //= 10
    return length


number = int(input('Введите число: '))
digits_sum = get_digits_sum(number)
number_length = get_number_length(number)
print('Сумма чисел:', digits_sum)
print('Количество цифр в числе:', number_length)
print('Разность суммы и количества цифр:', digits_sum - number_length)
