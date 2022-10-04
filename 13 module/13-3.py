def reverse(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        number //= 10
        reversed_number *= 10
        reversed_number = reversed_number + digit
    return reversed_number


number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
numbers_sum = int(reverse(number_1)) + int(reverse(number_2))
print(f'\nПервое число наоборот: {reverse(number_1)}')
print(f'Второе число наоборот: {reverse(number_2)}')
print(f'\nСумма {numbers_sum}')
print(f'Сумма наоборот: {reverse(numbers_sum)}')