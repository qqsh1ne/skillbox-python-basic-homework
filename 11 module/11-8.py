ONE_HOUR_ANGLE = 360 / 12
angle = float(input("Укажите угол часовой стрелки: "))
print(f'Угол поворота минутной стрелки = {angle % ONE_HOUR_ANGLE * 12} градусов.')