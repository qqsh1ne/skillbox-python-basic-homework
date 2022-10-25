goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product_name in goods:
    product_code = goods[product_name]
    item_total_quantity = 0
    item_total_cost = 0
    for product in store[product_code]:
        item_total_cost += product['quantity'] * product['price']
        item_total_quantity += product['quantity']
    print(f'{product_name} - {item_total_quantity} шт, общая стоимость {item_total_cost} рублей')