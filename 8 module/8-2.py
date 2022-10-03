debtors, sum_debt = int(input('Введите количество должников: ')), 0
for debtor in range(0, debtors + 1, 5):
    print(f'Должник с номером {debtor}')
    sum_debt += int(input('Сколько должны? '))
print(f'Общая сумма долга: {sum_debt}')