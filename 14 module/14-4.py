def reverse_float_number(number):
    int_part = int(number)
    float_part_len = len(str(number)) - len(str(int(number))) - 1
    float_part = int(number * 10 ** float_part_len % 10 ** float_part_len)

    return float(str(reverse_int_number(int_part)) + '.' + str(reverse_int_number(float_part)))


def reverse_int_number(number):
    result = ''
    while number > 0:
        result += str(number % 10)
        number //= 10
    return int(result)


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

first_number_reversed = reverse_float_number(first_number)
second_number_reversed = reverse_float_number(second_number)

print('Первое число наоборот:', first_number_reversed)
print('Второе число наоборот:', second_number_reversed)
print('Сумма:', first_number_reversed + second_number_reversed)
