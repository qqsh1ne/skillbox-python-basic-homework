orders_count = int(input('Введите кол-во заказов: '))
orders = {}

for i in range(1, orders_count + 1):
    order_data = input(f'{i} заказ: ').split()
    surname, pizza_name, quantity = order_data[0], order_data[1], int(order_data[2])
    if surname not in orders:
        orders[surname] = {pizza_name: quantity}
    else:
        if pizza_name not in orders[surname]:
            orders[surname][pizza_name] = quantity
        else:
            orders[surname][pizza_name] += quantity

for surname in sorted(orders):
    print(f'{surname}:')
    for pizza in sorted(orders[surname]):
        print('\t', pizza, orders[surname][pizza])
        