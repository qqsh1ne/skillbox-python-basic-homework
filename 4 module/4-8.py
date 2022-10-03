hours = int(input('Введите колличество часов: '))
debt = int(input('Введите задолженность: '))
money = int(input('Введите затраты на еду: '))
salary = 200 * hours / 2 ** 3 + hours
if salary >= debt + money:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся поработать!')
