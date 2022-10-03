text = input('Введите зашифрованное сообщение: ')
odd, even = '', ''
count = 0
for symbol in text:
    count += 1
    if count % 2 == 1:
        odd += symbol
    else:
        even = symbol + even
print(f'Расшифрованное сообщение: {odd + even}')