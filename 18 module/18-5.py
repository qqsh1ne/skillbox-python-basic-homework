def contains_upper_letter(text):
    for sym in text:
        if sym.isupper():
            return True
    return False


def get_digits_count(text):
    digits_count = 0
    for sym in text:
        if sym.isdigit():
            digits_count += 1
    return digits_count


while True:
    password = input('Придумайте пароль: ')

    if (len(password) < 8) or not contains_upper_letter(password) or (get_digits_count(password) < 3):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break

