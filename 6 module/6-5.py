ticket = int(input('Введите номер билета: '))
first_half = ticket // 1000
second_half = ticket % 1000
first_half_sum = 0
second_half_sum = 0
while first_half > 0:
    first_half_sum += first_half % 10
    first_half = first_half // 10
while second_half > 0:
    second_half_sum += second_half % 10
    second_half = second_half // 10
if first_half_sum == second_half_sum:
    print('Билет счастливый!')
else:
    print('Билет несчастливый :(')