letter_side_length = int(input('Введите размер стороны письма: '))
count = 0
while letter_side_length > 12:
    letter_side_length /= 2
    count += 1
print(f'Письмо нужно сложить {count} раз')