def reverse_number(number):
    if number != 0:
        text = ''
        while number > 0:
            text += str(number % 10)
            number = number // 10
        reverse_num = int(text)
        print('Число наоборот:', reverse_num)
        reverse_number(int(input('Введите число: ')))
    else:
        print('Программа завершена!')


reverse_number(int(input('Введите число: ')))
