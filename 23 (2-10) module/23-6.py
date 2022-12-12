user_name = input('Как вас зовут? ')
with open('chat.txt', 'w') as chat:
    chat.close()

while True:
    print('1 - увидеть текущий текст чата\n2 - написать сообщение')
    response = input('Введите 1 или 2: ')
    if response == '1':
        try:
            with open('chat.txt', 'r') as chat:
                print(''.join(chat.readlines()))
        except FileNotFoundError:
            print('Чат пуст\n')
    elif response == '2':
        new_msg = input('Введите сообщение: ')
        with open('chat.txt', 'a') as chat:
            chat.write(f'{user_name}: {new_msg}\n')
    else:
        print('Неизвестная команда\n')