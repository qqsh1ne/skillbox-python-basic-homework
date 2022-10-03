students = int(input('Введите количество учеников: '))
excellent, good, satisfactory = 0, 0, 0
for student in range(students):
    grade = int(input('Какую оценку получил ученик? '))
    if grade == 5:
        excellent += 1
    elif grade == 4:
        good += 1
    else:
        satisfactory += 1
if (excellent > good) and (excellent > satisfactory):
    print('Больше отличников!')
elif (good > excellent) and (good > satisfactory):
    print('Больше ударников')
else:
    print('Больше троечников :(')