import os
import string


def get_index(char, shift, alphabet):
    index = alphabet.index(char)
    if index + shift > len(alphabet) - 1:
        index += shift - len(alphabet)
    else:
        index += shift
    return index


def encrypt_string(text):
    encrypted_string = ''
    line_count = 0
    for row in text:
        line_count += 1

        for symbol in row:
            if symbol in ascii_ru:
                encrypted_string += ascii_ru[get_index(symbol, line_count, ascii_ru)]
            elif symbol in ascii_en:
                encrypted_string += ascii_en[get_index(symbol, line_count, ascii_en)]
            else:
                encrypted_string += symbol

    return encrypted_string


ascii_en = [i for i in string.ascii_letters]
ascii_ru = [chr(i) for i in range(ord('а'), ord('я') + 1)] + [chr(i) for i in range(ord('А'), ord('Я') + 1)]

text = open(os.path.abspath('text.txt'), 'r')

encrypted_string = encrypt_string(text)

text = open(os.path.abspath('cipher_text.txt'), 'w')
text.write(encrypted_string)
text.close()
