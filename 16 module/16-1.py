main = [1, 5, 3]
first_sideline = [1, 5, 1, 5]
second_sideline = [1, 3, 1, 5, 3, 3]

main.extend(first_sideline)
fives_count = main.count(5)
print('Кол-во цифр 5 при первом объединении:', fives_count)
for _ in range(fives_count):
    main.remove(5)

main.extend(second_sideline)
threes_count = main.count(3)
print('Кол-во цифр 3 при первом объединении:', threes_count)

print('Итоговый список:', main)