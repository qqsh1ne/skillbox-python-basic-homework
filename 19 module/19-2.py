data = {}

for i in range(int(input('Кол-во стран: '))):
    value = input(f'{i + 1} страна: ').split()
    for city in value[1:]:
        data[city] = value[0]

for i in range(3):
    city = input(f'\n{i + 1} город: ')
    country = data.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')