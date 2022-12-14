import random


class PlayerCard:
    def __init__(self, cost_card, name_card):
        self.cost_card = cost_card
        self.name_card = name_card


class Player:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points


class Game:
    sum_points = 0

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_one_turn(self, card_1, card_2):
        if self.sum_points > 21:
            cards[12].cost_card = 1
            self.player_1.points += card_1.cost_card
            self.player_2.points += card_2.cost_card
            print(self.player_1.points, card_1.name_card)
        else:
            self.player_1.points += card_1.cost_card
            self.player_2.points += card_2.cost_card
            self.sum_points = (self.player_1.points + self.player_2.points)
            print(self.player_1.points, card_1.name_card)

    def get_winner(self):
        if self.player_1.points > 21 and self.player_2.points > 21:
            print('Ничья. У обоих перебор.')
            print(f'{self.player_1.__name}, набрал {self.player_1.points} очков. {self.player_2.__name} набрал {self.player_2.points} очков.')
        elif self.player_1.points > 21 or self.player_2.points > self.player_1.points:
            print(f'Победил {self.player_2.__name}, набрав {self.player_2.points} очков. У {self.player_1.__name} {self.player_1.points} очков.')
        elif self.player_2.points > 21 or self.player_1.points > self.player_2.points:
            print(f'Победил {self.player_1.__name}, набрав {self.player_1.points} очков. У {self.player_2.__name} {self.player_2.points} очков.')
        elif self.player_1.points == self.player_2.points:
            print(f'Ничья! У обоих игроков {self.player_1.points} очков.')
        else:
            print('Нет победителей.')


cards = [PlayerCard(2, 'Двойка'), PlayerCard(3, 'Тройка'), PlayerCard(4, 'Четвёрка'), PlayerCard(5, 'Пятёрка'),
         PlayerCard(6, 'Шестёрка'), PlayerCard(7, 'Семёрка'), PlayerCard(8, 'Восьмёрка'), PlayerCard(9, 'Девятка'),
         PlayerCard(10, 'Десятка'), PlayerCard(10, 'Валет'), PlayerCard(10, 'Дама'), PlayerCard(10, 'Король'),
         PlayerCard(11, 'Туз')]

player = Player('Игрок')
dealer = Player('Диллер')
game = Game(player, dealer)

for _ in range(2):
    game.play_one_turn(cards[random.choice(range(0, 12))], cards[random.choice(range(0, 12))])

while True:
    request = int(input('1 - взять ещё карту, 2 - чтобы остановиться: '))
    if request == 1:
        game.play_one_turn(cards[random.randint(0, 12)], cards[random.randint(0, 12)])
    else:
        break
    if player.points > 21 or dealer.points > 21:
        break

game.get_winner()
