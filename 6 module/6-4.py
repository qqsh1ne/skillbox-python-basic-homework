months = 0
while True:
    days = int(input('Введите колличество дней в месяце: '))
    if days == 0:
        break
    if days % 2 == 0:
        months += 1
print('Количество месяцев с четным кол-вом дней: ', months)
