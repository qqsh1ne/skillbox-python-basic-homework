import os

text = input('Введите строку: ')
folder = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').replace(' ', os.path.sep)
file_name = input('Введите имя файла: ')
if not file_name.endswith('.txt'):
    file_name += '.txt'
path = os.path.join(os.path.sep, folder, file_name)

if os.path.exists(path):
    answer = input('Вы действительно хотите перезаписать файл (Да/Нет)? ').lower()
    if answer == 'да':
        new_file = open(path, 'w')
        new_file.write(text)
        new_file.close()
        print('Файл успешно перезаписан!')
    else:
        print('Вы отказались от перезаписи файла.')
else:
    new_file = open(path, 'w')
    new_file.write(text)
    new_file.close()
    print('Файл успешно сохранён!')
