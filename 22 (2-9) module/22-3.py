import string


def get_min_letter_frequency(chars):
    chars_dict = {}
    for char in chars:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    min_frequency = chars_dict['a']
    min_frequency_letter = 'a'
    for key in chars_dict:
        if chars_dict[key] < min_frequency:
            min_frequency = chars_dict[key]
            min_frequency_letter = key

    return min_frequency_letter


file = open('zen.txt')

zen = file.read()
file_words = zen.split()
file.seek(0)
file_lines = file.readlines()
chars = [i.lower() for i in zen if i in string.ascii_letters]

print(f'Количество букв в файле: {len(chars)}')
print(f'Количество слов в файле: {len(file_words)}')
print(f'Количество строк в файле: {len(file_lines)}')
print(f'Наиболее редкая буква: {get_min_letter_frequency(chars)}')
