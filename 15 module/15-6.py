word = input('Введите слово: ')
unique_letters = []

for letter in word:
    if letter in unique_letters:
        unique_letters.remove(letter)
    else:
        unique_letters.append(letter)

print('Количество уникальных букв:', len(unique_letters))