import random


class Warrior:
    def __init__(self, name: str, power: int = 20, health: int = 100):
        self.name = name
        self.power = power
        self.health = health

    def attack(self, warrior):
        print(f'{self.name} атаковал {warrior.__name}!')
        warrior.damage(self.power)

    def damage(self, power):
        self.health -= power

        if not self.health <= 0:
            print(f'У {self.name} осталось {self.health} здоровья!')
        else:
            print(f'{self.name} мертв')


def fight(war_1, war_2):
    while war_1.health > 0 and war_2.health > 0:
        if random.randint(0, 1) == 0:
            war_1.attack(war_2)
        else:
            war_2.attack(war_1)


warrior_1 = Warrior('Воин 1')
warrior_2 = Warrior('Воин 2')

fight(warrior_1, warrior_2)
