reverse_timer, is_stopped, seconds_left = int(input('Укажите кол-во секунд подогрева: ')), 0, 0
for i in range(reverse_timer, 0, - 1):
    print(f'Осталось {i} секунд')
    stop = int(input('Хотите прервать режим подогрева? 1 - Да, 0 - Нет: '))
    if stop == 1:
        is_stopped, seconds_left = 1, i
        break
if is_stopped == 1:
    print(f'Ваша еда готова, можете забрать, осталось {seconds_left} сек.')
else:
    print('Ваша еда готова, осторожно горячo!')
