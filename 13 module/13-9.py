def print_period_info():
    print('Период:', year)
    print('Остаток долга на начало периода:', current_debt)
    print('Выплачено процентов:', percent)
    print('Выплачено тела кредита:', debt_payment)
    print()


credit_debt = float(input('Введите сумму кредита: '))
credit_years = int(input('На сколько лет выдан? '))
credit_percent = int(input('Сколько процентов годовых? ')) / 100
years_before_changes = 3

current_debt = credit_debt

K = credit_percent * (1 + credit_percent) ** credit_years / ((1 + credit_percent) ** credit_years - 1)
A = round(K * credit_debt, 2)
for year in range(1, years_before_changes + 1):
    percent = current_debt * credit_percent
    debt_payment = A - percent
    print_period_info()
    current_debt -= debt_payment

print('=' * 30)

credit_years += int(input('На сколько лет продлевается договор? '))
years_left = credit_years - 3
credit_percent = int(input('Увеличение ставки до: ')) / 100

K = credit_percent * (1 + credit_percent) ** credit_years / ((1 + credit_percent) ** credit_years - 1)
A = round(K * current_debt, 2)

for year in range(1, years_left + 1):
    percent = current_debt * credit_percent
    debt_payment = A - percent
    print_period_info()
    current_debt -= debt_payment
