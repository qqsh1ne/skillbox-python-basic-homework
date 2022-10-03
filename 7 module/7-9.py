previous_salary = 0
is_rising = 1
for month in range(1, 11):
    salary = int(input(f'Введите зарплату за {month} месяц: '))
    if previous_salary > salary:
        print('Зарплата не увеличивается.')
        is_rising = 0
        break
    previous_salary = salary
if is_rising == 1:
    print('Зарплата увеличивается.')