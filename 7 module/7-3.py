salary_per_year = 0
for month in range(1, 13):
    salary_month = int(input(f'Введите зарплату за {month} месяц: '))
    salary_per_year += salary_month
print('Средняя зарплата за месяц', salary_per_year / 12, 'рублей')
