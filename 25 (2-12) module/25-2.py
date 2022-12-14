import random


class KillError(Exception):
    """
    Класс ошибки убийства. Родитель: Exception
    """
    pass


class DrunkError(Exception):
    """
    Класс ошибки пьянства. Родитель: Exception
    """
    pass


class CarCrashError(Exception):
    """
    Класс ошибки попадания в аварию. Родитель: Exception
    """
    pass


class GluttonyError(Exception):
    """
    Класс ошибки обжорства. Родитель: Exception
    """
    pass


class DepressionError(Exception):
    """
    Класс ошибки депрессии. Родитель: Exception
    """
    pass


class Buddhist:
    """
    Класс буддиста.

    Args:
        karma - Начальная карма (по умолчанию 0)
    """
    def __init__(self, karma=0):
        self.__karma = karma

    def get_karma(self):
        """
        Геттер для получения кармы.

        :return: karma
        :rtype: int
        """
        return self.__karma

    def set_karma(self, karma):
        """
        Сеттер для добавления кармы.

        :rtype: int
        """
        self.__karma += karma


def one_day():
    if random.randint(1, 10) == 1:
        raise random.choice([DrunkError('Напился'),
                             KillError('Убил'),
                             GluttonyError('Обжорство'),
                             CarCrashError('Попал в аварию'),
                             DepressionError('Депрессия')])
    else:
        return random.randint(1, 7)


with open('karma.log', 'w', encoding='utf8') as karma_log:
    karma_log.close()

max_karma = 500
buddhist = Buddhist()
day = 0
while buddhist.get_karma() < max_karma:
    day += 1
    try:
        buddhist.set_karma(one_day())
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as err:
        with open('karma.log', 'a', encoding='utf8') as karma_log:
            error_message = f'{err.__class__.__name__}. {err}'
            karma_log.write(f'День {day}. {error_message}\n')
else:
    print('Максимум кармы достигнут!')