line_number = 0
symbol_count = 0
people_data = []

try:
    with open('people.txt', 'r', encoding='utf8') as data_file:
        for line in data_file:
            line_number += 1
            length = len(line)
            if line.endswith('\n'):
                length -= 1
            try:
                symbol_count += length
                if length < 3:
                    raise Exception(f'Ошибка: менее трёх символов в строке {line_number}.')
            except Exception as exception:
                print(exception)
except Exception as exception:
    print(exception)
else:
    print('Общее количество символов:', symbol_count)
