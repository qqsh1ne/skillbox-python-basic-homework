educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
total_expenses = expenses
budget = educational_grant
for month in range(9):
    expenses += 3 * (expenses / 100)
    total_expenses += expenses
    budget += educational_grant
print(f'У родителей необходимо попросить: {total_expenses - budget} рублей')