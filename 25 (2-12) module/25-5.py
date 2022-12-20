import random
import math


class Car:
    """
    Класс машины

    Args:
        x, y - начальные координаты машины
        direction - направление (угол поворота)

    Attributes:
        __x, __y - начальные координаты машины
        __direction - направление (угол поворота)
    """
    def __init__(self, x: int, y: int, direction: float):
        self.__x = x
        self.__y = y
        self.__direction = direction

    def __str__(self):
        return f'Координаты: X={round(self.__x, 2)} Y={round(self.__y, 2)}\nУгол {round(self.__direction, 2)}'

    def move(self, distance):
        """
        Команда машине проехать distance не меняя направления

        :param distance: дистанция, которую необходимо проехать
        """
        self.__x = self.__x + distance * math.cos(self.__direction)
        self.__y = self.__y + distance * math.sin(self.__direction)

    def change_direction(self, new_direction):
        """
        Команда машине изменить направление

        :param new_direction: Новый угол поворота
        """
        self.__direction = new_direction


class Bus(Car):
    """
    Класс автобуса. Родитель: Car

    Args:
        x, y - начальные координаты автобуса
        direction - направление (угол поворота)

    Attributes:
        __x, __y - начальные координаты автобуса
        __direction - направление (угол поворота)
    """
    __MONEY_PER_PASSENGER = 3
    __DISTANCE_COEFFICIENT = 0.1

    def __init__(self, x: int, y: int, direction: float):
        super().__init__(x, y, direction)
        self.__passengers = 0
        self.__money = 0

    def __str__(self):
        return '\n'.join((f'{super().__str__()}', f'В автобусе {self.__passengers} пассажиров.', f'У водителя {round(self.__money, 2)} денег.'))

    def move(self, distance):
        """
        Команда автобусу проехать distance не меняя направления.
        Также произойдет перерасчет имеющихся у водителя денег с учетом расстояния

        :param distance: дистанция, которую необходимо проехать
        """
        self.__money += self.__MONEY_PER_PASSENGER * self.__passengers * distance * self.__DISTANCE_COEFFICIENT
        super().move(distance)

    def enter(self, passengers: int):
        """
        Команда автобусу принять passengers пассажиров.

        :param passengers: количество входящих пассажиров
        """
        self.__passengers += passengers

    def exit(self, passengers: int):
        """
        Команда автобусу высадить passengers пассажиров.
        Количество пассажиров не может стать меньше 0

        :param passengers: количество выходящих пассажиров
        """
        if passengers > self.__passengers:
            self.__passengers = 0
        else:
            self.__passengers -= passengers

    def get_passengers(self):
        """
        Геттер для поулчения текущего количества пассажиров

        :return: __passengers
        :rtype: int
        """
        return self.__passengers


car = Car(3, 10, 90)
bus = Bus(0, 0, 0)

print('Машина\n')

for i_time in range(1, 10):
    if random.randint(1, 2) == 1:
        car.move(random.randint(1, 100))
    else:
        car.change_direction(random.randint(0, 360))
    print(car)

print('\nАвтобус\n')

for i_time in range(1, 10):
    random_action = random.randint(1, 3)
    if random_action == 1 and bus.get_passengers() > 0:
        bus.exit(random.randint(1, 10))
    elif random_action == 2:
        bus.enter(random.randint(1, 10))

    if random.randint(1, 2) == 1:
        bus.change_direction(random.randint(0, 360))
    bus.move(random.randint(0, 360))
    print(bus)
