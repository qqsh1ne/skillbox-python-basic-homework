violations = 0
for sector in range(30, 36):
    people = int(input(f'Сколько людей в секторе {sector}? '))
    if people > 10:
        print('Нарушение! Слишком много людей в секторе!')
        violations += 1
    else:
        print('Всё спокойно.')
print('Количество нарушений:', violations)