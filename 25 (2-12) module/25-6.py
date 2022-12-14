import random


class House:
    """
    Класс дома, где живет семья

    Args:
        family - семья, живущая в доме
        money - изначальное количество денег (по ум. 100)
        food - изначальное кол-во еды в холодильнике (по ум. 50)
        cat_food - изначальное кол-во кошачьей еды (по ум. 30)
        dirt - изначальное количество грязи (по ум. 0)

    Attributes:
        family - семья, живущая в доме
        money - количество денег
        food - кол-во еды в холодильнике
        cat_food - кол-во кошачьей еды
        dirt - количество грязи
        earned - всего денег заработано
        food_eaten - всего еды съедено
        cat_food_eaten - всего кошачьей еды съедено
        fir_coats_bought - всего куплено шуб
    """
    def __init__(self, family, money: int = 100, food: int = 50, cat_food: int = 30, dirt: int = 0):
        self.family = family
        self.money = money
        self.food = food
        self.cat_food = cat_food
        self.dirt = dirt
        self.earned = 0
        self.food_eaten = 0
        self.cat_food_eaten = 0
        self.fur_coats_bought = 0

    def live_day(self):
        """
        Прожить один день (по правилам игры)
        """
        for i_resident in self.family:
            if self.dirt >= 90 and not isinstance(i_resident, Cat):
                i_resident.change_happiness(-10)

            if isinstance(i_resident, Cat) and self.cat_food >= 20 <= i_resident.satiety:
                i_resident.eat()

            elif isinstance(i_resident, Cat):
                if random.randint(1, 2) == 1:
                    i_resident.tear_up_wallpapers()
                else:
                    i_resident.sleeping()

            elif (isinstance(i_resident, Husband) or
                  isinstance(i_resident, Wife)) \
                    and self.food >= 60 and i_resident.satiety <= 30:
                i_resident.eat()
                print(i_resident.get_name(), 'поел(а)')

            elif isinstance(i_resident, Husband):
                if self.money <= 150:
                    husband.work()
                elif husband.happiness <= 50:
                    husband.game()
                elif husband.happiness <= 70:
                    husband.care_cat()
                else:
                    husband.work()

            elif isinstance(i_resident, Wife):
                if self.food <= 60 and self.money >= 100:
                    wife.buy_food()
                elif self.cat_food <= 20 and self.money >= 50:
                    wife.buy_cat_food()
                elif self.dirt >= 50:
                    wife.cleaning()
                elif wife.happiness <= 70:
                    wife.care_cat()
                elif self.money >= 450:
                    wife.buy_fur_coat()
                else:
                    wife.care_cat()

            elif isinstance(i_resident, Baby):
                if i_resident.satiety <= 40:
                    baby.eat()
                elif i_resident.happiness <= 25:
                    baby.sleeping()
                else:
                    baby.game()

    def check_for_death(self):
        """
        Проверяет, умер ли кто-то из семьи от голода или депрессии
        """
        for resident in self.family:
            if resident.satiety <= 0:
                print(f'{resident.__name} умер от голода')
                return True
            elif resident.happiness < 10 and not isinstance(resident, Cat):
                print(f'{resident.__name} умер от депрессии')
                return True
            return False

    def print_summary(self):
        """
        Выводит итоговую статистику за год
        """
        print(f'\nЗа год:'
              f'\nКуплено шуб: {self.fur_coats_bought}'
              f'\nЗаработано денег: {self.earned}'
              f'\nСъедено еды: {self.food_eaten}'
              f'\nКот съел еды: {self.cat_food_eaten}')


class Resident:
    """
    Класс члена семьи

    Args:
        name - имя
        satiety - изначальная сытость

    Attributes:
        name - имя
        satiety - сытость
    """
    def __init__(self, name: str, satiety: int):
        self.__name = name
        self.satiety = satiety

    def get_name(self):
        """
        Геттер для имени

        :return: name - имя члена семьи
        :rtype: str
        """
        return self.__name

    def eat(self):
        """
        Приём пищи членом семьи
        """
        self.satiety += 30
        house.food -= 30
        house.food_eaten += 30

    def loss_satiety(self, amount: int = 10):
        """
        Снижение сытости у члена семьи

        :param amount: Количество снижаемой сытости
        """
        self.satiety -= amount


class Husband(Resident):
    """
    Класс мужа. Родитель: Resident

    Args:
        name - имя
        satiety - изначальная сытость
        salary - зарплата
        happiness - изначальное счастье

    Attributes:
        name - имя
        satiety - сытость
        salary - зарплата
        happiness - счастье
    """
    def __init__(self, name: str, satiety: int = 30, salary: int = 150, happiness: int = 100):
        super().__init__(name, satiety)
        self.salary = salary
        self.happiness = happiness

    def change_happiness(self, happiness: int):
        """
        Изменение количества счастья у члена семьи

        :param happiness: Количество изменяемого счастья
        """
        self.happiness += happiness

    def work(self):
        """
        Пойти на работу. Увеличивает кол-во денег
        """
        self.loss_satiety()
        house.money += self.salary
        house.earned += self.salary
        print(f'{self.__name} сходил на работу')

    def care_cat(self):
        """
        Погладь кота. Добавляет счастье
        """
        self.loss_satiety()
        self.change_happiness(5)
        print(f'{self.__name} погладил кота')

    def game(self):
        """
        Поиграть в Dota 2. Увеличивает счастье
        """
        self.loss_satiety()
        self.change_happiness(20)
        print(f'{self.__name} поиграл в доту')


class Wife(Resident):
    """
    Класс жены. Родитель: Resident

    Args:
        name - имя
        satiety - изначальная сытость
        happiness - изначальное счастье

    Attributes:
        name - имя
        satiety - сытость
        happiness - счастье
    """
    def __init__(self, name: str, satiety: int = 30, happiness: int = 100):
        super().__init__(name, satiety)
        self.happiness = happiness

    def change_happiness(self, happiness: int):
        """
        Изменение количества счастья у члена семьи

        :param happiness: Количество изменяемого счастья
        """
        self.happiness += happiness

    def buy_food(self):
        """
        Сходить в магазин за едой. - деньги, + еда.
        """
        self.loss_satiety()
        house.money -= 100
        house.food += 100
        print(f'{self.__name} сходила в магазин за продуктами')

    def buy_cat_food(self):
        """
        Сходить в магазин за кошачьей едой. - деньги, + еда.
        """
        self.loss_satiety()
        house.money -= 50
        house.cat_food += 50
        print(f'{self.__name} сходила в магазин за едой для кота')

    def care_cat(self):
        """
        Погладь кота. Добавляет счастье
        """
        self.loss_satiety()
        self.change_happiness(5)
        print(f'{self.__name} погладила кота')

    def buy_fur_coat(self):
        """
        Купить шубу. - деньги, + счастье и шуба
        """
        self.loss_satiety()
        self.change_happiness(60)
        house.money -= 350
        house.fur_coats_bought += 1
        print(f'{self.__name} купила шубу')

    def cleaning(self):
        """Прибраться дома"""
        house.dirt -= 100
        if house.dirt < 0:
            house.dirt = 0
        self.satiety -= 10
        print(f'{self.__name} навела порядок в доме')


class Cat(Resident):
    """
    Класс кота. Родитель: Resident

    Args:
        name - имя
        satiety - изначальная сытость

    Attributes:
        name - имя
        satiety - сытость
    """
    def __init__(self, name: str, satiety: int = 30):
        super().__init__(name, satiety)

    def eat(self):
        """
        Поесть. Добавляет сытость, убирает корм
        """
        self.satiety += 20
        house.cat_food -= 10
        house.cat_food_eaten += 10
        print(f'{self.__name} поел(а).')

    def sleeping(self):
        """
        Поспать
        """
        self.loss_satiety()
        print(f'{self.__name} поспал(а)')

    def tear_up_wallpapers(self):
        """
        Рвать обои. Загрязняет дом
        """
        self.loss_satiety()
        house.dirt += 5
        print(f'{self.__name} подрал(а) обои')


class Baby(Resident):
    """
    Класс ребенка. Родитель: Resident

    Args:
        name - имя
        satiety - изначальная сытость
        happiness - изначальное счастье

    Attributes:
        name - имя
        satiety - сытость
        happiness - счастье
    """
    def __init__(self, name: str, satiety: int = 30, happiness: int = 100):
        super().__init__(name, satiety)
        self.happiness = happiness

    def change_happiness(self, happiness: int):
        """
        Изменение степени счастья у члена семьи

        :param happiness: Количество измененного счастья
        """
        self.happiness += happiness

    def game(self):
        """
        Поиграть. Восстанавливает счастье
        """
        self.loss_satiety()
        self.change_happiness(20)
        print(f'{self.__name} поиграл(а) в игру')

    def sleeping(self):
        """
        Поспать. Восстанавливает счастье
        """
        self.loss_satiety()
        self.change_happiness(30)
        print(f'{self.__name} поспал(а)')


def play_game():
    for i_day in range(1, 366):
        print(f'День {i_day}')
        house.dirt += 5
        if house.check_for_death():
            print('\nЭксперимент провалился :с')
            house.print_summary()
            exit()
        house.live_day()

    print('\nЭксперимент удался!')
    house.print_summary()


husband = Husband('Пудж')
wife = Wife('Квопа')
baby = Baby('Инвокер')
cat = Cat('Лион')
family_list = [husband, wife, baby, cat]
house = House(family_list)
play_game()




