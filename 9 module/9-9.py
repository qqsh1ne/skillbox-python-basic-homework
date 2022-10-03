stalls = input('Введите строку из 10 символов, где: a - свободное стойло, b - занятое: ')
milk, stall_number = 0, 0

for i in stalls:
    stall_number += 1
    if i == 'b':
        milk += stall_number * 2

print(f'Кол-во молока за день: {milk}')