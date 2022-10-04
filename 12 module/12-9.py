import random


def rock_paper_scissors():
    print('=' * 15)
    while True:
        answer = ['камень', 'ножницы', 'бумага']
        x = random.choice(answer)
        request = int(input('Камень - 1, ножницы - 2, бумага - 3 : '))
        print('У меня', x)
        if request == 1 and x == 'ножницы' or request == 2 and x == 'бумага' or request == 3 and x == 'камень':
            print('Ты выиграл!!!')
        elif answer[request - 1] == x:
            print('Ничья!')
        else:
            print('Ты проиграл!')
        print()
        if int(input('Хочешь выйти?\nЖми - 1\nПовторить - 2: ')) == 1:
            print('Игра окончена.')
            break
        print()


def guess_the_number():
    difficulty = int(input('Какой уровень сложности выберете?\nЛегкий - 1\nСложный - 2 : '))
    max_random = 10
    if difficulty == 2:
        max_random = 100
    x = random.randrange(1, max_random)
    print()
    number = int(input(f'Угадай число от 1 до {max_random} : '))

    while True:
        if x == number:
            print('Ты выиграл!!!')
            break
        number = int(input('Не угадал. Попробуй снова: '))


def main_menu():
    while True:
        choice = int(input('Во что хотите сыграть?\n"Камень, ножницы, бумага" - 1\n"Угадай число" - 2\nВыйти - 3 : '))
        if choice == 1:
            rock_paper_scissors()
        elif choice == 2:
            guess_the_number()
        elif choice == 3:
            print('Выход из игры...')
            break
        else:
            print('Неверный выбор!')
        print('=' * 15)


main_menu()
