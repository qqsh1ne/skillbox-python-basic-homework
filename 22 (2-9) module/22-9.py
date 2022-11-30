import zipfile


def is_in_alphabet(char):
    return ord('a') <= ord(char) <= ord('z') or ord('а') <= ord(char) <= ord('я') \
           or ord('A') <= ord(char) <= ord('Z') or ord('А') <= ord(char) <= ord('Я')


def get_frequency(text):
    chars_dict = {}
    chars_count = 0

    for char in text:
        if is_in_alphabet(char):
            chars_dict[char] = chars_dict.get(char, 0) + 1
            chars_count += 1

    frequency = [(char, "{:5.3f}".format(chars_dict[char] / chars_count)) for char in chars_dict.keys()]
    frequency.sort(key=lambda x: x[0])
    frequency.sort(key=lambda x: x[1], reverse=True)
    return frequency


archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
archive.extractall()
archive.close()

book = open('voyna-i-mir.txt', 'r', encoding='utf8').read()
frequency = get_frequency(book)
for char_data in frequency:
    print(char_data[0] + " " + char_data[1])
