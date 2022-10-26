def is_poly(string):
    chars = {}
    for i_sym in string:
        chars[i_sym] = chars.get(i_sym, 0) + 1

    odd_count = 0
    for i_value in chars.values():
        if i_value % 2 != 0:
            odd_count += 1

    return odd_count < 2


if is_poly(input('Введите строку')):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')