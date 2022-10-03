text = input('Введите текст сообщения: ')
count = 0

for char in text:
    count += 1
    if char == '*':
        print(f'* находится на {count} месте')
        break