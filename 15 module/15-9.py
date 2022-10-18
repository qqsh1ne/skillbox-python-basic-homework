word = input('Введите слово: ')
word_length = len(word)
is_palindrome = True

for i_letter in range(word_length // 2):
    if word[i_letter] != word[word_length - i_letter - 1]:
        is_palindrome = False
        break

print('Слово является палиндромом' if is_palindrome else 'Слово не является палиндромом')