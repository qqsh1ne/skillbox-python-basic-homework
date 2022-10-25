words_list = input('Введите строку: ').split()
max_length = -1
max_length_word = ''

for word in words_list:
    if len(word) > max_length:
        max_length = len(word)
        max_length_word = word

print('Самое длинное слово:', max_length_word)
print('Длина этого слова:', max_length)