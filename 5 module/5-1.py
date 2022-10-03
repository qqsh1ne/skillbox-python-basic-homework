exp = int(input('Введите количество очков: '))
level = 0
if exp < 1000:
    level = 1
elif exp < 2500:
    level = 2
elif exp < 5000:
    level = 3
else: 
    level = 4
print('Ваш уровень:', level)