def caesar_cipher(message, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    non_ciphering_symbols = ' !"#$%&`()*+,-./\\|0123456789:;<=>?@'
    return ''.join([(alphabet[(alphabet.index(symbol) + shift) % len(alphabet)] if symbol not in non_ciphering_symbols else symbol) for symbol in message])


print('Зашифрованное сообщение:', caesar_cipher(input('Введите сообщение: '), int(input('Введите сдвиг: '))))