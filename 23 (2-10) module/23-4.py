def is_valid(string):
    if line == '\n':
        return False
    data = string.split()
    if len(data) < 3:
        raise IndexError('Должны присутствовать все три поля')
    else:
        if not data[0].isalpha():
            raise NameError('Поле «Имя» должно содержать только буквы')
        if '@' not in data[1] or '.' not in data[1]:
            raise SyntaxError('Поле «Имейл» должно содержать @ и точку')
        if not data[2].isdigit():
            raise ValueError('Поле «Возраст» должно являться числом')
        elif int(data[2]) < 10 or int(data[2]) > 99:
            raise ValueError('Поле «Возраст» должно являться числом от 10 до 99')
    return True


file_reg_name = 'registrations.txt'
file_good_name = 'registrations_good.log'
file_bad_name = 'registrations_bad.log'
row_number = 0

file_good = open(file_good_name, 'w', encoding='utf8')
file_good.close()
file_bad = open(file_bad_name, 'w', encoding='utf8')
file_bad.close()

with open(file_reg_name, 'r', encoding='utf8') as f_registration, \
        open(file_good_name, 'a', encoding='utf8') as file_good, \
        open(file_bad_name, 'a', encoding='utf8') as file_bad:
    for line in f_registration:
        row_number += 1
        try:
            if is_valid(line):
                file_good.write(line)
        except (IndexError, NameError, SyntaxError, ValueError):
            file_bad.write(line)
