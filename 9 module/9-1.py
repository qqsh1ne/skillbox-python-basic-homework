count = 0
day_of_week = input('Введите день недели: ').lower()

for day in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'):
    count += 1
    if day == day_of_week:
        print(f'Номер дня недели: {count}')
        break