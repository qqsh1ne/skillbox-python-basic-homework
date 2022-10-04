def start_game():
    first_num = int(input("Введите первое число: "))
    second_num = int(input("Введите второе число: "))
    if len(str(first_num)) < 3 or len(str(second_num)) < 4:
        print('В первом числе должно быть не меньше трёх цифр.\nВо втором числе должно быть не меньше четырёх '
              'цифр.\nНачните игру заново')
        exit()
    else:
        return find_sum(first_num), find_sum(second_num)


def find_sum(num):
    num_length = len(str(num))
    last_digit = num % 10
    first_digit = num // 10 ** (num_length - 1)
    between_digits = num % 10 ** (num_length - 1) // 10
    return last_digit * 10 ** (num_length - 1) + between_digits * 10 + first_digit


first_n, second_n = start_game()

print(f'Изменённое первое число: {first_n}')
print(f'Изменённое второе число: {second_n}')
print(f'Сумма чисел: {first_n + second_n}')