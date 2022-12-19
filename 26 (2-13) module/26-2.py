import os


user_path = input('Введите путь директории: ')
start_path = user_path if user_path != '' else os.path.abspath(os.path.join('/'))
my_path = input('Введите имя директории: ')

gen_files_path = (link + '\\' + file
                  for link, dirs, files in list(os.walk(start_path)) if link.split('\\')[-1] == my_path
                  for file in files)

for my_path in gen_files_path:
    print(my_path)
