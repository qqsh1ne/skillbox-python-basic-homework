russian_score = int(input('Введите кол-во баллов по русскому языку: '))
maths_score = int(input('Введите кол-во баллов по математике: '))
it_score = int(input('Введите кол-во баллов по информатике: '))
if russian_score + maths_score + it_score >= 270:
    print('Поздравляю, ты поступил на бюджет')
else:
    print('К сожалению, ты не прошёл на бюджет')
