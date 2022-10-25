text = input('Введите текст: ')
frequency_dict = {}
inverted_frequency_dict = {}

for sym in text:
    if sym in frequency_dict:
        frequency_dict[sym] += 1
    else:
        frequency_dict[sym] = 1

print('Оригинальный словарь частот:')
for i_sym in sorted(frequency_dict.keys()):
    print(i_sym, ': ', frequency_dict[i_sym])

for number in frequency_dict.values():
    inverted_frequency_dict[number] = []
for symbol in frequency_dict:
    number = frequency_dict[symbol]
    inverted_frequency_dict[number].append(symbol)

print('Инвертированный словарь частот:')
for i in inverted_frequency_dict:
    print(i, ': ', inverted_frequency_dict[i])
