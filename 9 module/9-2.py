given_word = 'карамба'
count = 0
for pirat in range(10):
    if input('Введите слово: ').lower() == given_word:
        count += 1

print(count)
