months, food_left = 0, 100
for kilogram in range(food_left - 4, -1, -4):
    months += 1
    print(f'{months} месяц\nГречки осталось {kilogram} кг')
print('Гречка кончилась!')
