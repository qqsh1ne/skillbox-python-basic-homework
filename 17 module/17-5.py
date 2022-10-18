text = input('Введите строку: ')

temp = text[text.find('h') + 1:text.rfind('h')]
print(temp[::-1])
