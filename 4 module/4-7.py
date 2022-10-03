available_money = int(input('Введите сумму, которую хотите снять: '))
if available_money % 100 == 0:
    print('OK')
else:
    print('Такую сумму снять невозможно. Обратитесь в другой банкомат.')
