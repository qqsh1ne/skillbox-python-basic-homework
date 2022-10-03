import math

EARTH_VOLUME = 10.8321 * 10 ** 11
random_planet_radius = float(input('Введите радиус случайной планеты: '))
V = (4 / 3) * math.pi * random_planet_radius ** 3
earth_to_planet_relation = round(EARTH_VOLUME / V, 3)

if EARTH_VOLUME > V:
    print('Объём планеты Земля больше в', earth_to_planet_relation, 'раз')
else:
    print('Объём планеты Земля меньше в (1/' + str(earth_to_planet_relation) + ') =', round(V / EARTH_VOLUME, 3), 'раз')