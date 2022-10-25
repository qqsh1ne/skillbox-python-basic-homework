text = input('Введите строку: ')

print('Результат: ', ' '.join(word.capitalize() for word in text.split()))
