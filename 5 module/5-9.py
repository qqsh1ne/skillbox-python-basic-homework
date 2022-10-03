salary = int(input('Введите доход: '))
tax = 0
if salary > 50000:
    tax = (salary - 50000) * 0.3 + (50000 - 10000) * 0.2 + 10000 * 0.13
elif 10000 < salary < 50000:
    tax = (salary - 10000) * 0.2 + 10000 * 0.13
else:
    tax = salary * 0.13
print(tax)
