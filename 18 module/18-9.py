import string


text = input('Сообщение: ').split()
result = ''

for word in text:
    temp = ''
    reversed_word = ''
    for sym in word:
        if sym in string.punctuation:
            reversed_word = ''.join([reversed_word, temp[::-1], sym])
            temp = ''
        else:
            temp = ''.join([temp, sym])

    result = ''.join([result, reversed_word, temp[::-1], ' '])

print('Новое сообщение:', result)
