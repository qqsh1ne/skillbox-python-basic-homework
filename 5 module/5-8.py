flat_price = int(input('Введите стоимость квартиры: '))
area = int(input('Введите площадь квартиры: '))

if (flat_price <= 10000000 and area >= 100) or (flat_price <= 7000000 and area >= 80):
    print('Квартира подходит.')
else:
    print('Квартира не подходит.')