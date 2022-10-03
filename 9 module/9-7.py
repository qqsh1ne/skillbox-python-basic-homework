text = input('Введите текст: ')
word_length = 0
max_word_length = 0
for char in text:
    if char != ' ':
        word_length += 1
    else:
        word_length = 0
    if max_word_length < word_length:
        max_word_length = word_length

print(f'Самое длинное слово, букв: {max_word_length}')