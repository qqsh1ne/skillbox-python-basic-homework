import os


def line_count(file_name: str) -> int:
    count = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if line != "\n" and not line.startswith('#'):
                count += 1
    return count


path = input('Введите путь для сканирования: ')
find_file = (line_count(file) for file in os.listdir(path) if file.endswith('.py'))
print(sum([str_count for str_count in find_file]))
