import os


def file_sizes(path):
    files_stat = {'size': 0, 'files': 0, 'subdirs': 0}

    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            files_stat['size'] += os.path.getsize(file_path)
            files_stat['files'] += 1
        else:
            result = file_sizes(os.path.abspath(os.path.join(path, i_elem)))
            files_stat['size'] += result['size']
            files_stat['files'] += result['files']
            files_stat['subdirs'] += 1
    return files_stat


path = os.path.abspath(os.path.join('..', '22 (2-9) module'))

result = file_sizes(path)
print(path)
print(f'Размер каталога (в Кб): {round(result["size"] / 1024, 2):,}'.replace(',', ' '))
print(f'Количество файлов: {result["files"]:,}'.replace(',', ' '))
print(f'Количество подкаталогов: {result["subdirs"]:,}'.replace(',', ' '))
