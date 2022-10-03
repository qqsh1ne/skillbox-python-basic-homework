boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))
order = ''
if boys > 2 * girls or girls > 2 * boys:
    print('Решения нет')
elif boys >= girls:
    difference = boys - girls
    for bgb in range(difference):
        order += 'BGB'
    for bg in range(girls - difference):
        order += 'BG'
else:
    difference = girls - boys
    for bgb in range(difference):
        order += 'GBG'
    for bg in range(boys - difference):
        order += 'GB'
print('Рассадить в порядке:', order)