number = int(input('Введите число: '))
digit_quantity = 0
while True:
    digit_quantity += 1
    number = number // 10
    if number == 0:
        break
print('В числе ' + str(digit_quantity) + ' цифр!')