text = input('Введите строку: ')

str_len = len(text)
result = ''
i_letter = 0
while i_letter < str_len:
    counter = 0
    curr_char = text[i_letter]
    while i_letter < str_len and text[i_letter] == curr_char:
        i_letter += 1
        counter += 1
    result = ''.join([result, ''.join([curr_char, str(counter)])])

print('Закодированная строка:', result)