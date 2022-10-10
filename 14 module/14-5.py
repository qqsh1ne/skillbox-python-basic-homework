number = int(input('Введите число: '))

for divider in range(2, number + 1):
    if number % divider == 0:
        print('Наименьший делитель, отличный от единицы:', divider)
        break