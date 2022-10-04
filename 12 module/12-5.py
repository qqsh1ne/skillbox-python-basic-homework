def count_letters():
    text = input('Введите текст: ').lower()
    number = input('Какую цифру ищем? ')
    letter = input('Какую букву ищем? ')
    numbers_count = 0
    letters_count = 0
    for char in text:
        if number == char:
            numbers_count += 1
        if letter == char:
            letters_count += 1
    print(f'Количество цифр {number}: {numbers_count}')
    print(f'Количество букв {letter}: {letters_count}')


count_letters()
