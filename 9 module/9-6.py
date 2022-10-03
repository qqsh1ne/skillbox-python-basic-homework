string = input('Введите строку: ')
substring_length = 0
max_substring = 0

for char in string:
    if char == 's':
        substring_length += 1
    else:
        substring_length = 0
    if max_substring < substring_length:
        max_substring = substring_length
print(f'Самая длинная последовательность: {max_substring}')
