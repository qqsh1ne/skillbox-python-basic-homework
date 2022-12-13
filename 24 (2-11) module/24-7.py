import random


class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money


class Human:
    def __init__(self, name, house: House, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety

    def eat(self):
        self.satiety += 90
        self.house.food -= 5

    def work(self):
        self.satiety -= 15
        self.house.money += 50

    def play(self):
        self.satiety -= 20

    def buy_food(self):
        self.house.food += 35
        self.house.money -= 20

    def is_alive(self):
        return self.satiety > 0

    def live_day(self):
        cube_number = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.buy_food()
        elif self.house.money < 50:
            self.work()
        elif cube_number == 1:
            self.work()
        elif cube_number == 2:
            self.eat()
        else:
            self.play()


class Game:
    def __init__(self, days_to_live):
        self.days_to_live = days_to_live

    def play(self, human_1: Human, human_2: Human):
        for i_day in range(self.days_to_live):
            if human_1.is_alive():
                human_1.live_day()
            if human_2.is_alive():
                human_2.live_day()

            if not human_1.is_alive() and not human_2.is_alive():
                print('Все умерли :ссс')
                break

        if human_1.is_alive() and human_2.is_alive():
            print('Все выжили!')
        elif human_1.is_alive():
            print(f'Выжил только {human_1.name}.')
        elif human_2.is_alive():
            print(f'Выжил только {human_2.name}.')


game = Game(365)

default_house = House()
default_human_1 = Human('Вася', default_house)
default_human_2 = Human('Петя', default_house)
game.play(default_human_1, default_human_2)

game = Game(365)
house = House(1000, 1000)
human_1 = Human('Вася', house)
human_2 = Human('Петя', house)
game.play(human_1, human_2)

game = Game(365)
zero_house = House(0, 0)
zero_human_1 = Human('Вася', zero_house, 0)
zero_human_2 = Human('Петя', zero_house, 0)
game.play(zero_human_1, zero_human_2)